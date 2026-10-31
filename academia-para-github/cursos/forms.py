from django import forms
from .models import Curso, Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descripcion', 'profesor', 'estudiantes']
        labels = {
            'titulo': 'Título del Curso',
            'descripcion': 'Descripción',
            'profesor': 'Profesor Asignado (ForeignKey)',
            'estudiantes': 'Estudiantes Inscritos (ManyToManyField)',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Programación Python'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del curso...'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
            'estudiantes': forms.CheckboxSelectMultiple(),
        }


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email']
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Ana Torres'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ana@correo.com'}),
        }
