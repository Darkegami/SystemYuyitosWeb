from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home ,name='home'),
    path('producto/', producto ,name='producto'),
    path('carro/', carro ,name='carro'),
    path('agregarProducto/', agregarProducto ,name='agregarProducto'),
    path('iniciarSesion/', iniciarSesion ,name="iniciarSesion"),
    path('crearCliente/', crearCliente ,name="crearCliente"),
    path('fichaCliente/', fichaCliente ,name="fichaCliente"),
]