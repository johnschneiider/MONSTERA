from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_promociones, name='mostrar_promociones'),
]
