from django.shortcuts import render, HttpResponse
from CursosApp.models import Curso, UnidadCurso
from django.http import JsonResponse



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
