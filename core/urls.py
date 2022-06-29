from tabnanny import verbose
from unicodedata import name
from django.urls import path
from .views import inicio, cuenta, feriados, formularioContacto, galeria, quienes_somos, registrarse, crud, form_producto, form_mod_producto, form_del_producto, crud_cliente, form_mod_cliente, form_cliente, form_del_cliente, adminF


urlpatterns = [
    path('', inicio, name="inicio"),
    path('cuenta/', cuenta, name='cuenta'),
    path('feriados/', feriados, name="feriados"),
    path('formularioContacto/', formularioContacto, name="formularioContacto"),
    path('galeria/', galeria,name="galeria"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('registrarse/', registrarse, name="registrarse"),
    path('crud/', crud, name="crud"),
    path('form_producto/',form_producto, name="form_producto"),
    path('form_mod_producto/<id>',form_mod_producto,name="form_mod_producto"),
    path('form_del_producto/<id>',form_del_producto,name="form_del_producto"),
    path('crud_cliente/',crud_cliente,name="crud_cliente"),
    path('form_mod_cliente/<id>',form_mod_cliente,name="form_mod_cliente"),
    path('form_cliente/',form_cliente,name="form_cliente"),
    path('form_del_cliente/<id>',form_del_cliente,name="form_del_cliente"),
    path('adminF/',adminF,name="adminF"),
]