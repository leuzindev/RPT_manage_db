from django.shortcuts import redirect
from rest_framework import serializers

class Validate:
    
    def usuarioValido(nome, email, senha, senha2):
        if not nome.strip():
            raise serializers.ValidationError({'NOME':"O campo não pode ser vazio"})
        if not email.strip():
            raise serializers.ValidationError({'E-MAIL':"O campo não pode ser vazio"})
        if senha != senha2:
            raise serializers.ValidationError({'SENHA':"As senhas não são iguais"})
    
    def loginValido(email, senha):
        if not email.strip():
            raise serializers.ValidationError({'E-MAIL':"O campo não pode ser vazio"})
        if not senha.strip():
            raise serializers.ValidationError({'SENHA':"O campo não pode ser vazio"})