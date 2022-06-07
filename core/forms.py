from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Usuario, Producto


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre','email','contrasena',]


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['categoria','nombreProduc','precio','descripcion','sku',]