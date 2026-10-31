from django.contrib import admin
from .models import Curso, Profesor, Estudiante


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'total_cursos')
    search_fields = ('nombre', 'email')
    ordering = ('nombre',)

    @admin.display(description='Cursos asignados')
    def total_cursos(self, obj):
        return obj.cursos.count()


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'total_cursos')
    search_fields = ('nombre', 'email')
    ordering = ('nombre',)

    @admin.display(description='Cursos inscritos')
    def total_cursos(self, obj):
        return obj.cursos.count()


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'profesor', 'total_estudiantes')
    list_filter = ('profesor',)
    search_fields = ('titulo', 'descripcion', 'profesor__nombre')
    filter_horizontal = ('estudiantes',)
    list_select_related = ('profesor',)
    ordering = ('titulo',)

    @admin.display(description='Estudiantes inscritos')
    def total_estudiantes(self, obj):
        return obj.estudiantes.count()
