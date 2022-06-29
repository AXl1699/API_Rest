from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Cliente, Producto 


class ProductoForm(ModelForm):

    
    class Meta: 
        model = Producto
        fields =['id_producto','nombre_producto','precio','categoria']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields =['id_cliente','nombre_cliente','correo_cliente','telefono_cliente','direccion_cliente']