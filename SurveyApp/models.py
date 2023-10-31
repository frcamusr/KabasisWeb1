from django.db import models
from django.conf import settings
from CursosApp.models import Curso, UnidadCurso  # Asegúrate de importar los modelos correctos

class Question(models.Model):
    id=models.AutoField(primary_key=True)
    # crear el campo question_type con solo las opciones de texto y opción múltiple
    question_type = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255, null=True )
    option_b = models.CharField(max_length=255 , null=True)
    option_c = models.CharField(max_length=255, null=True)
    option_d = models.CharField(max_length=255, null=True)
    correct_answer = models.CharField(max_length=1, null=True)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  # Campo de clave foranea para curso_id
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)  # Campo de clave foranea para unidad_id


    def __str__(self):
        return self.id
    
# crear el modelo Answer con los campos question, user, text_answer y option_answer
class Answer(models.Model):
    id=models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=255, null=True)
    #option answer puede ser nulo
    option_answer = models.CharField(max_length=1, null=True)
    def __str__(self):
        return self.id
    

