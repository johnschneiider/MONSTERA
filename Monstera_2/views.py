from django.shortcuts import render
from productos.models import Producto_Core
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.contrib.auth import views as auth_views


def inicio(request):
    productos = Producto_Core.objects.all()
    return render(request, 'index.html', {'productos': productos})

class CustomLogoutView(auth_views.LogoutView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return super().post(request, *args, **kwargs)