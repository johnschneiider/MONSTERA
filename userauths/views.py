from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauths.forms import userRegisterForms
from django.contrib.auth import views as auth_views
from userauths.forms import userRegisterForms, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.views import View
import random

User = settings.AUTH_USER_MODEL

from django.contrib import messages


from django.shortcuts import redirect

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Ya habías iniciado sesión")
        return redirect("/")  # Redirigir a la página principal o a donde desees

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Iniciaste sesión exitosamente")
                return redirect('/')
            else:
                messages.warning(request, "Email o contraseña incorrectos. Intenta nuevamente.")
        else:
            messages.error(request, "Formulario no válido. Por favor, verifica los campos e intenta nuevamente.")
    else:
        form = LoginForm()

    return render(request, "userauths/sign-in.html", {'form': form})





def inicio(request):
    return render(request, 'login.html') # aqui se redirige cuando se cierra sesion en la plataforma


class CustomLogoutView(View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Has cerrado sesión exitosamente.")
        return redirect('userauths:inicio')
    

def sign_up(request):
    if request.method == 'POST':
        form = userRegisterForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = userRegisterForms()
    return render(request, 'userauths/sign-up.html', {'form': form})



    
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Has cerrado sesión exitosamente.")
        return redirect('userauths:inicio')
    

def logout_view(request):
    django_logout(request)
    return render(request, 'inicio.html')