# Generated by Django 5.1.1 on 2024-09-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(verbose_name='Descripción del producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del producto')),
                ('photo', models.ImageField(upload_to='productos', verbose_name='Foto del producto')),
            ],
        ),
    ]
