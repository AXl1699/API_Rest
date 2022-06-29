from operator import is_not
from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ClienteForm, ProductoForm

def adminF(request):
    return render(request, 'adminF.html')

# Create your views here.
def crud_cliente(request):
    clientes=Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'crud_cliente.html', datos)

def form_cliente(request):
    datos ={
        'form':ClienteForm()
    }
    if request.method== 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardados Correctamente"
            
    return render(request,'form_cliente.html',datos)

def form_del_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    cliente.delete()
    return redirect(to="crud_cliente")
    
def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(id_cliente=id)
    datos = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST,instance=cliente)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado Correctamente"
    return render(request, 'form_mod_cliente.html',datos)



def crud(request):
    productos=Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'crud.html', datos)


def form_producto(request):
    datos ={
        'form':ProductoForm()
    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardados Correctamente"
            
    return render(request,'form_producto.html',datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    return redirect(to="crud")
    
def form_mod_producto(request, id):
    producto = Producto.objects.get(id_producto=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado Correctamente"
    return render(request, 'form_mod_producto.html',datos)


def inicio(request):

    return render(request, 'inicio.html')

def cuenta(request):

    return render(request, 'cuenta.html')

def feriados(request):

    return render(request, 'feriados.html')

def formularioContacto(request):

    return render(request, 'formularioContacto.html')

def galeria(request):

    return render(request, 'galeria.html')

def quienes_somos(request):

    return render(request, 'quienes_somos.html')

def registrarse(request):

    return render(request, 'registrarse.html')