from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="cursos", null=True, blank=True)
    descripcion = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre
    

# Modelo para la tabla de Unidades de un Curso
class UnidadCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    orden = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo






    


