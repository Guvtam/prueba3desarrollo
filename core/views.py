from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm


# Create your views here.
def home(request):
    return render(request,'core/home.html')

def tienda(request):
    return render(request,'core/tienda.html')

def registroUsuario(request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request,'core/registroUsuario.html')


def registro(request):
    producto = Producto.objects.all()
    datos = {
        'producto' : producto
    }
    return render(request,'core/registro.html',datos)

def form_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request,'core/form_producto.html',datos)


def form_mod_producto(request, id):
    producto = Producto.objects.get(sku = id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request,'core/form_mod_producto.html',datos)

def form_del_producto(request,id):
    producto = Producto.objects.get(sku=id)
    producto.delete()
    return redirect(to="registro")