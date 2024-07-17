from django.db import models
from django.shortcuts import render


ESTADO_CHOICES = (
    ('activo', 'Activo'),
    ('agotado', 'Agotado'),
    ('descontinuado', 'Descontinuado'),
)


class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/galeria', default="pngegg_3.png", null=True, blank=True)
    
    def __str__(self):
        return self.title if self.title else 'Sin título'


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos/galeria', default="pngegg_3.png", null=True, blank=True)
    
    def __str__(self):
        return self.title if self.title else 'Sin título'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    talla = models.CharField(max_length=20, default=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    stock = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to='productos/galeria', default="pngegg_3.png", null=True, blank=True)
    imagen2 = models.ImageField(upload_to='productos/galeria',default="pngegg_3.png", null=True, blank=True)
    imagen3 = models.ImageField(upload_to='productos/galeria',default="pngegg_3.png", null=True, blank=True)
    imagen4 = models.ImageField(upload_to='productos/galeria',default="pngegg_3.png", null=True, blank=True)
    imagen5 = models.ImageField(upload_to='productos/galeria',default="pngegg_3.png", null=True, blank=True)
    valoracion_promedio = models.DecimalField(max_digits=3, decimal_places=1, default=4.7)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    precio_original = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, default=0)
    
    def __str__(self):
        return self.title if self.title else 'Sin título'

    def porcentaje(self):
        nuevo_precio = (self.precio_oferta / self.precio_original) * 100
        return nuevo_precio
    
    def revews(request):
        productos = Producto.objects.all()
        for producto in productos:
            producto.valoracion_porcentaje = (producto.valoracion_promedio / 5) * 100  # Calcular el porcentaje
        context = {"productos": productos}
        return render(request, 'core/lista-de-productos.html', context)
    
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.conf import settings
from userauths.models import User

STATUS_CHOICE = (
    ("publicado", "Publicado"),
    ("enviado", "Enviado"),
    ("entregado", "Entregado"),
)

STATUS = (
    ("en_proceso", "Procesando"),
    ("enviado", "Enviado"),
    ("devuelto", "Devuelto"),
    ("en_revision", "En_Revision"),
    ("publicado", "Publicado"),
)


RATING = (
    ( 1, "⭐☆☆☆☆"),
    ( 2, "⭐⭐☆☆☆"),
    ( 3, "⭐⭐⭐☆☆"),
    ( 4, "⭐⭐⭐⭐☆"),
    ( 5, "⭐⭐⭐⭐⭐"),
    )

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="categoria", alphabet="abcdefghijk123457890")
    title = models.CharField(max_length=100, default="Alimentos")
    image = models.ImageField(upload_to="category", default="categoria.jpg")
    featured = models.BooleanField(default=False)
    products_status = models.CharField(choices=STATUS, max_length=20, default="en revisión")
    
    class Meta:
        verbose_name_plural = "Categorias"
        
    def category_image(self):
        return mark_safe('<img src = "%s" width ="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title if self.title else 'Sin título'
    
class Tags(models.Model):
    pass
    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="vendedor", alphabet="abcdefghijk123457890")
    
    title = models.CharField(max_length=100, default="El Testificador")
    image = models.ImageField(upload_to=user_directory_path, default="producto.jpg")
    description = models.TextField(null=True, blank=True, default="Este es un vendedor maravilloso")
    
    adress = models.CharField(max_length=100, default="Avenida Siempre viva")
    contact = models.CharField(max_length=100, default="123 456 7890")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    autentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    waranty_period = models.CharField(max_length=100, default="100")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name_plural = "Vendedores"
    
    def vendor_image(self):
        return mark_safe('<img src = "%s" width ="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title if self.title else 'Sin título'
        
class Producto_Core(models.Model):
        pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijk123457890")
        
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        caterory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
        vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
        
        title = models.CharField(max_length=100, default="El mejor producto aqui")
        image = models.ImageField(upload_to=user_directory_path, default="produto.jpg")
        description = models.TextField(null=True, blank=True, default="Este es el producto")
        
        price = models.DecimalField(max_digits=10,decimal_places=0, default=200)
        old_price = models.DecimalField(max_digits=10,decimal_places=0, default=400)
        
        specifications = models.TextField(null=True, blank=True, default="Este es el producto")
        #tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
        
        products_status = models.CharField(choices=STATUS, max_length=20, default="en revisión")
        
        status = models.BooleanField(default=True)
        in_stock = models.BooleanField(default=True)
        featured = models.BooleanField(default=False)
        digital = models.BooleanField(default=False)
        
        sku = ShortUUIDField(unique=True, length=4, max_length=20, prefix="sku", alphabet="abcdefghijk123457890")
        
        date = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(null=True, blank=True)
        
        class Meta:
            verbose_name_plural = "Productos"
        
        def product_image(self):
            return mark_safe('<img src = "%s" width ="50" height="50" />' % (self.image.url))
        
        def __str__(self):
            return self.title if self.title else 'Sin título'
        
        def get_precentage(self):
            new_price = (self.price / self.old_price) * 100
            return new_price
        
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product.images", default="product.jpg")
    product = models.ForeignKey(Producto_Core, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
            verbose_name_plural = "Imagenes de Productos"


############################### Card, Order, OrderItems and Address #############################
############################### Card, Order, OrderItems and Address #############################
############################### Card, Order, OrderItems and Address #############################
############################### Card, Order, OrderItems and Address #############################


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default=200)
    paid_track = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    products_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="en revisión")
    
    class Meta:
        verbose_name_plural = "Cart Order"
    
    

class CartOrderItems(models.Model):
    user = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    products_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default=200)
    total = models.DecimalField(max_digits=999999999999999999, decimal_places=2, default=200)
    
    class Meta:
        verbose_name_plural = "Cart Order Items"
        
    def order_img(self):
        return mark_safe('<img src = "/media/%s" width ="50" height="50" />' % (self.image))
    
############################### Product Revew, WishLists, Address #############################
############################### Product Revew, WishLists, Address #############################
############################### Product Revew, WishLists, Address #############################
############################### Product Revew, WishLists, Address #############################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Producto_Core, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Productos Reviews"
    
    def __str__(self):
        return self.product.title if self.product.title else ' Sin titulo'
    
    def get_rating (self):
        return self.rating
    
    
class whishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Producto_Core, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Lista Deseos"
    
    def __str__(self):
        return self.product.title

    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Address"
    
    
    ################################### CARRITO DE COMPRAS #####################################


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito de {self.user.username}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Producto_Core, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_total_price(self):
        return self.quantity * self.product.price
