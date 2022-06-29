from pyexpat import model
from tabnanny import verbose

from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='id_categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombreCategoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='id_producto')
    nombre_producto = models.CharField(max_length=50, verbose_name='nombre_producto')
    precio = models.CharField(max_length=10, verbose_name='precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, verbose_name='id_cliente')
    nombre_cliente = models.CharField(max_length=50, verbose_name='nombre_cliente')
    correo_cliente = models.CharField(max_length=200, verbose_name='correo_cliente', null='no ingresado')
    telefono_cliente = models.IntegerField( verbose_name='telefono_cliente',null='no ingresado')
    direccion_cliente = models.CharField(max_length=200, verbose_name='direccion_cliente',null='no ingresado')

    def __str__(self):
        return self.nombre_cliente