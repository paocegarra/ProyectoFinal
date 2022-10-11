from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario_articulo(request):
    return render (request,"blog/formulario-articulo.html")


def procesar_formulario_seccion(request):
    return render (request,"blog/formulario-seccion.html")


def procesar_formulario_autor(request):
    return render (request,"blog/formulario-autor.html")