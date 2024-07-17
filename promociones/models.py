# En models.py de tu aplicación de promociones (por ejemplo, promotions/models.py)

from django.db import models

class Promocion(models.Model):  # Asegúrate de usar 'Promocion', no 'promociones'
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='promociones/')

    def __str__(self):
        return self.title