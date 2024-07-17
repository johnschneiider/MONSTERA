from django.shortcuts import render
from .models import Producto_Core,Category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from productos.models import Producto_Core

# def detalle_producto(request, producto_id):
#     #producto = Producto_Core.objects.get(id=producto_id)
#     producto = Producto_Core.objects.filter(featured=True).order_by("-id")
#     return render(request, 'core/shop-product-vendor.html', {'producto': producto})

# def category(request):
#     categories = Category.objects.filter(featured=True)  # Filtrar categorías destacadas
#     context = {"categories": categories}
#     return render(request, 'core/lista-de-productos.html', context)

def productos(request):
    productos = Producto_Core.objects.filter(products_status='publicado').order_by("-id")
    context = {"productos": productos}
    return render(request, 'core/lista-de-productos.html', context)

def product_list_views (request):
    productos = Producto_Core.objects.filter(products_status='publicado')
    context = {"productos": productos}
    return render(request, 'core/lista-de-productos.html', context)

def categoria (request):
    categoria = Category.objects.filter(products_status='publicado')
    context = {"categoria": categoria}
    return render(request, 'core/category-list.html', context)

def filtrar (request):
    filtrar = Producto_Core.objects.filter(products_status='publicado')
    context = {"filtrar": filtrar}
    return render(request, 'core/product-filter.html', context)

def categoria_productos (request, cid):
    categoria = Category.objects.get(cid=cid)
    productos = Producto_Core.objects.filter(products_status='publicado', caterory=categoria)
    context = {"productos": productos, "categoria": categoria}
    return render(request, 'core/product-category-list.html', context)

######################## CARRITO DE COMPRAS #########################

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Producto_Core, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('productos') 

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user, status='open')
    items = cart.items.all()
    total = sum(item.product.price * item.quantity for item in items)
    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'core/cart.html', context)

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')