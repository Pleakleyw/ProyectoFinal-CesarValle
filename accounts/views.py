from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages 

from .forms import RegistroForm
from recetas.models import Receta  # importa el modelo Receta

# Vista para mostrar el perfil del usuario
@login_required
def perfil_view(request):
    recetas = Receta.objects.filter(autor=request.user).order_by('-creado')
    return render(request, 'accounts/perfil.html', {
        'usuario': request.user,
        'recetas': recetas,
    })

# Vista para editar perfil
class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/perfil_editar.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('accounts:perfil')

    def get_object(self):
        return self.request.user

# Vista para registro de nuevos usuarios (sin login automático)
def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'¡Tu cuenta ha sido creada! Ahora puedes iniciar sesión.')
            return redirect('login')  # redirige al login
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})
