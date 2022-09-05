from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    """ Pagina de Login """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat= True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('home_list')

    return render(request,'login.html')


def home_list(request):
    """ pagina de listagem de produtos """
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


# def buscar(request):
    
#     buscar = request.GET.get('buscar')
    
#     if buscar:
        
#         list_products = Product.objects.filter(name__icontains=buscar)
    
#     products = get_object_or_404(Product, pk=product_id)
    
#     if 'buscar' in request.GET:
#         nome_a_buscar = request.GET['buscar']
#         if buscar:
#             products.filter(name__icontains=nome_a_buscar)
            
#     data = {
#         'products': products
#     }
    
#     return render(request, 'home_page.html', data)


