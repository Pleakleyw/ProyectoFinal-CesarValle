from django import forms
from .models import Receta, Comentario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'preparacion', 'presentacion', 'imagen', 'categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ej: Lomo saltado'
        })
        self.fields['ingredientes'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Lista los ingredientes...',
            'rows': 4,
        })
        self.fields['preparacion'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Explica cómo se prepara...',
            'rows': 4,
        })
        self.fields['presentacion'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Opcional: consejos de presentación, acompañamientos o tips del chef...',
            'rows': 3,
        })
        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['categoria'].widget.attrs.update({
            'class': 'form-control'
        })


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe un comentario...',
                'rows': 3
            }),
        }
