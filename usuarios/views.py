from django.shortcuts import render
# from .models import usuarios

def cadastro(request):
    
    return render(request, 'usuarios/cadastro.html')

def login(request):
    
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass