# Generated by Django 5.0.2 on 2024-03-17 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0008_alter_producto_categoria_alter_producto_imagen_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producto",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="productos.categoria"
            ),
        ),
        migrations.AlterField(
            model_name="producto",
            name="vendedor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="productos.vendedor"
            ),
        ),
    ]
