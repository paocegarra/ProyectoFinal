from django.contrib import admin
from django.urls import path, include

from blog.views import mostrar_inicio, procesar_formulario_articulo, procesar_formulario_seccion, procesar_formulario_disegnador

urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("formulario-diseñador/", procesar_formulario_disegnador),
    
    ]