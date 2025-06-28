from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # Editor enriquecido para preparación

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    ingredientes = models.TextField()
    preparacion = RichTextField()
    presentacion = models.TextField(blank=True, null=True, verbose_name="Presentación o notas adicionales")
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas_publicadas')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='recetas')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
        
class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=500)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.receta.titulo}'
