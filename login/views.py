from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from django.contrib import auth
from django.contrib.auth.models import User
from login.validator import Validate

def login(request):
    """ Pagina de Login """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        # Valida o Login
        if Validate.loginValido(email, senha):
            return redirect('/')
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat= True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('home_list')
            
    return render(request,'login.html')


def home_list(request):
    """ Pagina de listagem de produtos """
    if request.user.is_authenticated:
        products = Product.objects.order_by('id')
        data = {
            'products' : products
        }
        return render(request, 'home_list.html', data)
    else:
        return redirect('login')
        


def home_id(request, product_id):
    """ pagina de listagem de produtos pelo ID """
    if request.user.is_authenticated:
        products = get_object_or_404(Product, pk=product_id)

        data = {
            'products': products
        }

        return render(request,'home_page.html', data)   
    else:
        return redirect('login')
        

def logout(request):
    """ Realizar o logout """
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    """ Realiza o cadastro de um usuario """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        # Valida o Usuario
        if Validate.usuarioValido(nome, email, senha, senha2):
            return redirect('cadastro')
        if User.objects.filter(email = email).exists():
            return redirect('cadastro')
        
        # Cria o Usuario
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return redirect('login')
    else:
        return render(request, 'cadastro.html')
    

def buscar(request):
    
    lista_product = Product.objects.order_by('name')
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_products = lista_product.filter(name__icontains=nome_a_buscar)
            
    data = {
        'products': lista_products
    }
    
    return render(request, 'home_page.html', data)


