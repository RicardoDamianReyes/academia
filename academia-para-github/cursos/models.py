from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"
        
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    profesor = models.ForeignKey(
        Profesor, on_delete=models.SET_NULL, null=True, blank=True, related_name='cursos'
    )
    estudiantes = models.ManyToManyField(Estudiante, blank=True, related_name='cursos')

    def __str__(self):
        return self.titulo