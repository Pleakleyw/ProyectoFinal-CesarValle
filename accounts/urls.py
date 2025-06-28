from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import PerfilUpdateView, perfil_view, register_view
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('perfil/', login_required(perfil_view), name='perfil'),
    path('perfil/editar/', login_required(PerfilUpdateView.as_view()), name='perfil_editar'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm  # 👈 usa el login estilizado
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
