# Generated by Django 5.0.2 on 2024-03-03 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "productos",
            "0002_producto_imagen2_producto_imagen3_producto_imagen4_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="producto",
            name="valoracion_promedio",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="producto",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="productos.categoria"
            ),
        ),
    ]
