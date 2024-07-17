from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from productos.views import categoria, filtrar,categoria_productos

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
    path("admin/", admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('user/', include("userauths.urls")),
    path('sign-in/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('promociones/', include('promociones.urls')), 
    path('productos/', include('productos.urls')),
    path('categoria/', categoria, name='categoria'),
    path('filtrar/', filtrar, name='filtrar'),
    path('categoria/<cid>', categoria_productos, name='categoria_productos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)