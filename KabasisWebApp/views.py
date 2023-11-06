from django.shortcuts import render, HttpResponse
from CursosApp.models import Curso, UnidadCurso
from django.http import JsonResponse
# importar los modelos de la app SurveyApp
from SurveyApp.models import Question, Answer, Contenido, Quiz, Video, Actividad



# Create your views here.

def home(request):

    return render(request, "KabasisWebApp/home.html")



def tienda(request):

    return render(request, "KabasisWebApp/tienda.html")

def blog(request):

    return render(request, "KabasisWebApp/blog.html")

def contacto(request):

    return render(request, "KabasisWebApp/contacto.html")

def editContenido(request):
    cursos = Curso.objects.all()
    Unidad = UnidadCurso.objects.all()
    
    data = {

        'cursos': cursos,
        'unidad': Unidad,
    }
    return render(request, "KabasisWebApp/edit/editContenido.html" , data)

def obtener_unidades(request, curso_id):
    unidades = UnidadCurso.objects.filter(curso_id=curso_id).values('id','titulo')
    curso_nombre = Curso.objects.get(id=curso_id).nombre
    
    data = {
        'cursoNombre': curso_nombre,
        'unidades': list(unidades)
    }
    
    return JsonResponse(data)


# por cada unidad y curso enlistar los contenidos, quiz, videos y actividades desde la base de datos y modelos
def obtener_contenido(request, unidad_id):
    # obtener el contenido de la unidad
    contenido = Contenido.objects.filter(unidad_id=unidad_id).values('id','titulo','contenido')
    # obtener los videos de la unidad
    videos = Video.objects.filter(unidad_id=unidad_id).values('id','link')
    # obtener los quiz de la unidad
    quiz = Quiz.objects.filter(unidad_id=unidad_id).values('id','question_id')
    # obtener las actividades de la unidad
    actividades = Actividad.objects.filter(unidad_id=unidad_id).values('id','titulo','contenido')
    # listar lo anterior para mostrarlo en la vista
    data = {
        'contenido': list(contenido),
        'videos': list(videos),
        'quiz': list(quiz),
        'actividades': list(actividades)
    }
    # retornar la data en formato json para que pueda ser leida por javascript
    return JsonResponse(data)



