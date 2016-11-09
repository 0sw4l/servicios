from django.contrib import admin
from .models import Categoria, Comentario, Servicio, Usuario, Empresa
# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['id']