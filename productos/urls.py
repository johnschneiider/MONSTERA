from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    #path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    #path('', views.lista_de_productos, name='lista_de_productos'),
    path('', views.productos, name='productos'),
    path('categoria/', views.categoria, name='categoria'),
    path('/filtrar', views.filtrar, name='filtrar'),
    path('/categoria/<cid>', views.categoria_productos, name='categoria_productos'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='cart'),
]

# Configuración de archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
