# En admin.py de tu aplicación de promociones (promotions/admin.py)

from django.contrib import admin
from .models import Promocion

admin.site.register(Promocion)
