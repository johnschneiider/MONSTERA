from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Atributos personalizados si los hay
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    pass

# Solucionar colisiones de nombres
User._meta.get_field('groups').remote_field.related_name = 'user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions'
