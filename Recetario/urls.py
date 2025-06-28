from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Página de inicio y about
    path('recetas/', include('recetas.urls')),  # OJO: debe ser 'recetas', no 'recipes'
    path('accounts/', include('accounts.urls')),  # Registro personalizado
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
