from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def producto(request):
    return render(request, 'core/producto.html')

def carro(request):
    return render(request, 'core/carro.html')

def agregarProducto(request):
    return render(request, 'core/agregarProducto.html')

def iniciarSesion(request):
    return render(request, 'core/iniciarSesion.html')

def crearCliente(request):
    return render(request, 'core/crearCliente.html')

def fichaCliente(request):
    return render(request, 'core/fichaCliente.html')