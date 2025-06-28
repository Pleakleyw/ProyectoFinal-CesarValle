from django.shortcuts import render
from recetas.models import Receta  # Importamos el modelo

def home_view(request):
    recetas_top = Receta.objects.filter(imagen__isnull=False).order_by('?')[:4]  # aleatorio
    return render(request, "pages/home.html", {"recetas_top": recetas_top})

def about_view(request):
    return render(request, "pages/about.html")
