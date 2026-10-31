from django.urls import path
from . import views

urlpatterns = [
    # Rutas originales
    path('', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:pk>/', views.detalle_curso, name='detalle_curso'),
    path('profesores/', views.ProfesorListView.as_view(), name='lista_profesores'),

    # Rutas basadas en clases (CBV)
    path('web/cursos/', views.CursoListView.as_view(), name='web_lista_cursos'),
    path('web/cursos/<int:pk>/', views.CursoDetailView.as_view(), name='web_detalle_curso'),
    path('web/cursos/nuevo/', views.CursoCreateView.as_view(), name='web_crear_curso'),
    path('web/cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='web_editar_curso'),
    path('web/cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='web_eliminar_curso'),

    # Estudiantes (CRUD)
    path('web/estudiantes/', views.EstudianteListView.as_view(), name='web_lista_estudiantes'),
    path('web/estudiantes/nuevo/', views.EstudianteCreateView.as_view(), name='web_crear_estudiante'),
    path('web/estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name='web_detalle_estudiante'),
    path('web/estudiantes/<int:pk>/editar/', views.EstudianteUpdateView.as_view(), name='web_editar_estudiante'),
    path('web/estudiantes/<int:pk>/eliminar/', views.EstudianteDeleteView.as_view(), name='web_eliminar_estudiante'),

    # Reto del profesor
    path('web/profesores/<int:pk>/', views.ProfesorDetailView.as_view(), name='web_detalle_profesor'),
]