from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect

app_name = "userauths"

class CustomLogoutView(auth_views.LogoutView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/')
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return super().post(request, *args, **kwargs)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sign-in/', views.login_view, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('sign-up/', views.sign_up, name='sign_up'), 
]