from django.db import models
from django.conf import settings
from CursosApp.models import Curso, UnidadCurso  # Asegúrate de importar los modelos correctos

class Question(models.Model):
    QUESTION_TYPES = [
        ('option', 'Opción múltiple'),
        ('text', 'Texto'),
    ]
    
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPES)
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255, null=True)
    option_b = models.CharField(max_length=255, null=True)
    option_c = models.CharField(max_length=255, null=True)
    option_d = models.CharField(max_length=255, null=True)
    correct_answer = models.CharField(max_length=1, null=False)

    def __str__(self):
        return self.text
    
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
    
# crear el modelo contenido con los campos id, titulo, contenido, unidad, curso y una relación uno a muchos entre unidad y contenido
class Contenido(models.Model):
    id=models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.id

class Quiz(models.Model):
    #relacion uno a muchos entre question y quiz, además tiene los atributos id, question_id curso, unidad
    id=models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    def __str__(self):
        return self.id
    
# clase de video que solo contiene un enlace de youtube para cada unidad del curso, relacion muchos videos a una unidad
class Video(models.Model):
    id=models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    link = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.id
    
# clase de actividad que contiene una instancia de contenido, questions y answers, relacion muchos a uno entre actividad y unidad
class Actividad(models.Model):
    id=models.AutoField(primary_key=True)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    answers = models.ManyToManyField(Answer)
    unidad = models.ForeignKey(UnidadCurso, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.id

