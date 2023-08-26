from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import FormularioRegistro


# Create your views here.

def register_user(request):

    if request.method == "POST":
        registro=FormularioRegistro(request.POST)
        if registro.is_valid():
            registro.save()
            username= registro.cleaned_data["username"]
            password= registro.cleaned_data["password1"]
            user= authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, "Te has Registrado Correctamente!!!")
            return redirect('index')
    else:
        registro= FormularioRegistro()

    return render(request, 'autenticar/register_user.html',{'formulario':registro,})

def logout_user(request):
    logout(request)
    messages.success(request, "Has salido correctamente")
    return redirect("index")
 
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # para autenticar el user y pass
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user) 
            return redirect('index')
        else:
            messages.success(request,('Usuario o Contraseña Incorrecta'))
            return redirect("login")
    else:    
        return render(request,'autenticar/login.html')