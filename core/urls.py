from django.urls import path
from .views import home, registroUsuario,tienda,form_producto,form_mod_producto, registro,form_del_producto

urlpatterns = [
    path('',home,name="home"),
    path('registroUsuario',registroUsuario,name="registroUsuario"),
    path('tienda',tienda,name="tienda"),
    path('form-producto',form_producto,name="form_producto"),
    path('form-mod-producto/<id>',form_mod_producto,name="form_mod_producto"),
    path('registro', registro,name="registro"),
    path('form_del_producto/<id>',form_del_producto,name="form_del_producto"),


]