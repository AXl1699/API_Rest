# Generated by Django 4.0.5 on 2022-06-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cliente_correo_cliente_cliente_direccion_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono_cliente',
            field=models.IntegerField(max_length=200, null='no ingresado', verbose_name='telefono_cliente'),
        ),
    ]