from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Campos que se mostrarán en la lista de usuarios en el panel de administración
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Campos que se utilizarán para buscar usuarios en el panel de administración
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Campos que se utilizarán para filtrar usuarios en el panel de administración
    list_filter = ('is_staff', 'is_active', 'groups')

# Registrar el modelo User personalizado con su administrador personalizado
admin.site.register(User, CustomUserAdmin)
