from django.urls import path
from .views import (
    RecetaListView, RecetaDetailView,
    RecetaCreateView, RecetaUpdateView, RecetaDeleteView
)

app_name = 'recetas'

urlpatterns = [
    path('', RecetaListView.as_view(), name='lista'),
    path('nueva/', RecetaCreateView.as_view(), name='crear'),
    path('<slug:slug>/', RecetaDetailView.as_view(), name='detalle_receta'),
    path('<slug:slug>/editar/', RecetaUpdateView.as_view(), name='editar'),
    path('<slug:slug>/eliminar/', RecetaDeleteView.as_view(), name='eliminar'),
]
