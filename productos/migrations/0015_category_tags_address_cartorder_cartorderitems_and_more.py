# Generated by Django 5.0.2 on 2024-07-06 03:47

import django.db.models.deletion
import productos.models
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0014_alter_producto_precio_oferta_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijk123457890",
                        length=10,
                        max_length=20,
                        prefix="categoria",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="Alimentos", max_length=100)),
                (
                    "image",
                    models.ImageField(default="categoria.jpg", upload_to="category"),
                ),
            ],
            options={
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="Tags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=100, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Address",
            },
        ),
        migrations.CreateModel(
            name="CartOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=200, max_digits=999999999999999999
                    ),
                ),
                ("paid_track", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "products_status",
                    models.CharField(
                        choices=[
                            ("en_proceso", "Procesando"),
                            ("enviado", "Enviado"),
                            ("entregado", "Entregado"),
                        ],
                        default="en revisión",
                        max_length=30,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Cart Order",
            },
        ),
        migrations.CreateModel(
            name="CartOrderItems",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invoice_no", models.CharField(max_length=200)),
                ("products_status", models.CharField(max_length=200)),
                ("item", models.CharField(max_length=200)),
                ("image", models.CharField(max_length=200)),
                ("qty", models.IntegerField(max_length=200)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=200, max_digits=999999999999999999
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=200, max_digits=999999999999999999
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.cartorder",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Cart Order Items",
            },
        ),
        migrations.CreateModel(
            name="Producto_Core",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijk123457890",
                        length=10,
                        max_length=20,
                        prefix="",
                        unique=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(default="El mejor producto aqui", max_length=100),
                ),
                (
                    "image",
                    models.ImageField(
                        default="produto.jpg",
                        upload_to=productos.models.user_directory_path,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="Este es el producto", null=True
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=0, default="200", max_digits=99999999999999999
                    ),
                ),
                (
                    "old_price",
                    models.DecimalField(
                        decimal_places=0, default="400", max_digits=99999999999999999
                    ),
                ),
                (
                    "specifications",
                    models.TextField(
                        blank=True, default="Este es el producto", null=True
                    ),
                ),
                (
                    "products_status",
                    models.CharField(
                        choices=[
                            ("en_proceso", "Procesando"),
                            ("enviado", "Enviado"),
                            ("devuelto", "Devuelto"),
                            ("en_revision", "En_Revision"),
                            ("publicado", "Publicado"),
                        ],
                        default="en revisión",
                        max_length=20,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("in_stock", models.BooleanField(default=True)),
                ("featured", models.BooleanField(default=False)),
                ("digital", models.BooleanField(default=False)),
                (
                    "sku",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijk123457890",
                        length=4,
                        max_length=20,
                        prefix="sku",
                        unique=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                (
                    "caterory",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="productos.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default="Super producto",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "tags",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="productos.tags",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Productos",
            },
        ),
        migrations.CreateModel(
            name="ProductImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "images",
                    models.ImageField(
                        default="product.jpg", upload_to="product.images"
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="productos.producto_core",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Imagenes de Productos",
            },
        ),
        migrations.CreateModel(
            name="ProductReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review", models.TextField()),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "⭐☆☆☆☆"),
                            (2, "⭐⭐☆☆☆"),
                            (3, "⭐⭐⭐☆☆"),
                            (4, "⭐⭐⭐⭐☆"),
                            (5, "⭐⭐⭐⭐⭐"),
                        ],
                        default=None,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="productos.producto_core",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Productos Reviews",
            },
        ),
        migrations.CreateModel(
            name="Vendor4",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijk123457890",
                        length=10,
                        max_length=20,
                        prefix="vendedor",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(default="El Testificador", max_length=100)),
                (
                    "image",
                    models.ImageField(
                        default="producto.jpg",
                        upload_to=productos.models.user_directory_path,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="Este es un vendedor maravilloso", null=True
                    ),
                ),
                (
                    "adress",
                    models.CharField(default="Avenida Siempre viva", max_length=100),
                ),
                ("contact", models.CharField(default="123 456 7890", max_length=100)),
                ("chat_resp_time", models.CharField(default="100", max_length=100)),
                ("shipping_on_time", models.CharField(default="100", max_length=100)),
                ("autentic_rating", models.CharField(default="100", max_length=100)),
                ("days_return", models.CharField(default="100", max_length=100)),
                ("waranty_period", models.CharField(default="100", max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Vendedores",
            },
        ),
        migrations.CreateModel(
            name="whishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="productos.producto_core",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Lista Deseos",
            },
        ),
    ]
