from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Receta, Categoria, Comentario
from .forms import RecetaForm, ComentarioForm


class RecetaListView(ListView):
    model = Receta
    template_name = 'recetas/receta_list.html'
    context_object_name = 'recetas'
    ordering = ['-creado']
    paginate_by = 12  # ← Paginación: 12 recetas por página

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria__id=categoria_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['categoria_seleccionada'] = self.request.GET.get('categoria')
        return context


class RecetaDetailView(FormMixin, DetailView):
    model = Receta
    template_name = 'recetas/receta_detail.html'
    context_object_name = 'receta'
    form_class = ComentarioForm

    def get_success_url(self):
        return reverse('recetas:detalle_receta', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all().order_by('-creado')
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() and request.user.is_authenticated:
            comentario = form.save(commit=False)
            comentario.receta = self.object
            comentario.autor = request.user
            comentario.save()
            return redirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


class RecetaCreateView(LoginRequiredMixin, CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'recetas/receta_form.html'
    success_url = reverse_lazy('recetas:lista')

    def form_valid(self, form):
        receta = form.save(commit=False)
        receta.autor = self.request.user

        base_slug = slugify(receta.titulo)
        slug = base_slug
        counter = 1
        while Receta.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        receta.slug = slug

        receta.save()
        return super().form_valid(form)


class RecetaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'recetas/receta_form.html'
    success_url = reverse_lazy('recetas:lista')

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor


class RecetaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receta
    template_name = 'recetas/receta_confirm_delete.html'
    success_url = reverse_lazy('recetas:lista')

    def test_func(self):
        receta = self.get_object()
        return self.request.user == receta.autor
