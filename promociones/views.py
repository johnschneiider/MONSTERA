# En el archivo views.py de tu aplicación principal
from django.shortcuts import render
from promociones.models import Promocion  # Asegúrate de importar 'Promocion', no 'Promociones'

def mostrar_promociones(request):
    promociones = Promocion.objects.all()  # Asegúrate de usar 'Promocion', no 'Promociones'
    context = {
        'promociones': promociones,
    }
    return render(request, 'tu_app/promociones.html', context)
