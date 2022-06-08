from django.db import models

# Create your models here.

#modelo para Categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre Categoria')
    

    def __str__(self):
        return self.nombreCategoria



class Usuario(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre completo")
    email = models.CharField(primary_key=True, max_length=100,verbose_name="Email")
    contrasena = models.CharField(max_length=15, verbose_name="Contraseña")

    def __str__(self):
        return self.email

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProduc = models.CharField(max_length=20, verbose_name="Nombre Producto")
    precio = models.IntegerField(verbose_name="Precio Producto")
    descripcion = models.CharField(max_length=200,verbose_name="Descripcion Producto")
    sku = models.CharField(primary_key=True,max_length=30,verbose_name="Codigo Producto")

    def __str__(self):
        return self.sku