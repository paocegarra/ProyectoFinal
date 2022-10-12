from django.contrib import admin

from blog.models import Articulo, Disegnador, Seccion

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Disegnador)
admin.site.register(Seccion)
