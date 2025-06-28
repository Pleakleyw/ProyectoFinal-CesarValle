from django.contrib import admin
from .models import Receta, Categoria, Comentario

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'creado')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ['titulo', 'ingredientes']
    list_filter = ['creado', 'autor', 'categoria']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'receta', 'creado')
    search_fields = ('autor__username', 'contenido')
    list_filter = ('creado', 'receta')
