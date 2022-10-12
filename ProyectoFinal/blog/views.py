from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Articulo
from blog.forms import ArticuloForm, SeccionForm, AutorForm

# Create your views here.

def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario_articulo(request):
    
    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario" : mi_formulario}
        return render (request,"blog/formulario-articulo.html", context = contexto)
    
    if request.method == "POST":
        
        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo = datos_ingresados ["titulo"],
                texto = datos_ingresados ["texto"],
                fecha = datos_ingresados ["fecha"],    
            )
            
            nuevo_modelo.save()
            
        contexto = {"formulario" : mi_formulario}
        return render (request,"blog/formulario-articulo.html", context = contexto)

def procesar_formulario_seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario" : mi_formulario}
    return render (request, "blog/formulario-seccion.html", context = contexto)


def procesar_formulario_autor(request):
    mi_formulario = AutorForm()
    contexto = {"formulario" : mi_formulario}
    return render (request,"blog/formulario-autor.html", context = contexto)