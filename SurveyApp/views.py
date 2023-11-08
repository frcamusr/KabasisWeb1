from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import QuestionForm, AnswerForm, TextForm, VideoForm, ActividadForm
from .models import Question, Answer, Contenido, Quiz, Video, Actividad
from django.contrib.auth.decorators import login_required
from django.urls import reverse




# Preguntas: crear, eliminar y actualizar
def create_question(request, id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Question y asignar el quiz
            question = Question(quiz_id=id)
            question.question_type = form.cleaned_data['question_type']
            question.text = form.cleaned_data['text']
            question.option_a = form.cleaned_data['option_a']
            question.option_b = form.cleaned_data['option_b']
            question.option_c = form.cleaned_data['option_c']
            question.option_d = form.cleaned_data['option_d']
            question.correct_answer = form.cleaned_data['correct_answer']
            question.save()
            # Redirigir a la página del quiz
            return redirect(reverse('listar_quiz', args=[id]))
    else:
        form = QuestionForm()
    return render(request, 'crear_pregunta.html', {'form': form, 'id_quiz': id})



def delete_question(request, id):
    question = Question.objects.get(quiz_id=id)

    question.delete()
    return redirect(reverse('listar_quiz', args=[id]))


# def update_question, este tendra un formulario para actualizar la pregunta
def update_question(request, id):

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        question = Question.objects.get(quiz_id=id)
        tipo = question.question_type

        if form.is_valid():
            # guardar la pregunta y sus opciones, usando el id de la pregunta

            if tipo == 'text':
                #form = QuestionForm(initial={'text': question.text})
                # guardar las preguntas con el formulario de texto
                question.text = form.cleaned_data['text']
                question.save()
                return redirect(reverse('listar_quiz', args=[id]))

            else:
                #form = QuestionForm(initial={'text': question.text, 'option_a': question.option_a, 'option_b': question.option_b, 'option_c': question.option_c, 'option_d': question.option_d, 'correct_answer': question.correct_answer})

                question.text = form.cleaned_data['text']
                question.option_a = form.cleaned_data['option_a']
                question.option_b = form.cleaned_data['option_b']
                question.option_c = form.cleaned_data['option_c']
                question.option_d = form.cleaned_data['option_d']
                question.correct_answer = form.cleaned_data['correct_answer']
                question.save()
                return redirect(reverse('listar_quiz', args=[id]))
        else:
            if tipo == 'text':
                form = QuestionForm(initial={'text': question.text})
            else:
                form = QuestionForm(initial={'text': question.text, 'option_a': question.option_a, 'option_b': question.option_b, 'option_c': question.option_c, 'option_d': question.option_d, 'correct_answer': question.correct_answer})
        
   
    return render(request, 'update_question.html', {'form': form, 'question': question, 'tipo': tipo})



# mostrar los enlaces de todos los quiz creados para cada unidad y curso:
def listar_material(request, idCurso, unidad):
    quizzes = Quiz.objects.filter(curso_id=idCurso, unidad_id=unidad)
    # agregar variable para texto y video
    texto = Contenido.objects.filter(curso_id=idCurso, unidad_id=unidad)
    video = Video.objects.filter(curso_id=idCurso, unidad_id=unidad)
    actividad = Actividad.objects.filter(curso_id=idCurso, unidad_id=unidad)

    idCurso = idCurso
    unidad = unidad


    return render(request, 'listar_material.html', {'quizzes': quizzes, 'texto':texto, 'video':video, 'actividad':actividad, 'idCurso': idCurso, 'unidad': unidad})




#Quiz: crear, editar, eliminar y listar

def crear_quiz(request, idCurso, unidad):
    # creamos el quiz sin formulario directamente en la vista usando el modelo Quiz y idCurso y unidad como parametros
    quiz = Quiz()
    quiz.curso_id = idCurso
    quiz.unidad_id = unidad
    quiz.save()
    # redireccionamos a listar_contenido
    return redirect(reverse('listar_material', args=[idCurso, unidad]))

# edit_quiz solo envia a la lista de quiz
def edit_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    idCurso = quiz.curso_id
    unidad = quiz.unidad_id
    return redirect(reverse('listar_quiz', args=[quiz.id]))

# Eliminar quiz y sus preguntas
def delete_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    quiz.delete()
    return redirect(reverse('listar_material', args=[quiz.curso_id, quiz.unidad_id]))

def listar_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    idCurso = quiz.curso_id
    unidad = quiz.unidad_id
    questions = Question.objects.filter(quiz_id=id)
    return render(request, 'listar_quiz.html', {'questions': questions, 'quiz':quiz ,'idCurso': idCurso, 'unidad': unidad})



# Texto: crear, editar, eliminar
def crear_texto(request, idCurso, unidad):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Contenido y asignar el curso y unidad
            contenido = Contenido(curso_id=idCurso, unidad_id=unidad)
            contenido.titulo = form.cleaned_data['titulo']
            contenido.texto = form.cleaned_data['texto']
            contenido.save()
            # Redirigir a la página del quiz
            return redirect(reverse('listar_material', args=[idCurso, unidad]))
    else:
        form = TextForm()
    return render(request, 'crear_texto.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})
# editar texto
def editar_texto(request, id):
    contenido = Contenido.objects.get(id=id)
    idCurso = contenido.curso_id
    unidad = contenido.unidad_id
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            contenido.titulo = form.cleaned_data['titulo']
            contenido.texto = form.cleaned_data['texto']
            contenido.save()
            return redirect(reverse('listar_material', args=[idCurso, unidad]))
    else:
        form = TextForm(initial={'titulo': contenido.titulo, 'texto': contenido.texto})
    return render(request, 'editar_texto.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})
# eliminar texto
def eliminar_texto(request, id):
    contenido = Contenido.objects.get(id=id)
    contenido.delete()
    return redirect(reverse('listar_material', args=[contenido.curso_id, contenido.unidad_id]))

# Video: crear, editar, eliminar
def crear_video(request, idCurso, unidad):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Contenido y asignar el curso y unidad
            video = Video(curso_id=idCurso, unidad_id=unidad)
            video.titulo = form.cleaned_data['titulo']
            video.link = form.cleaned_data['link']
            video.descripcion = form.cleaned_data['descripcion']
            video.save()
            # Redirigir a la página del quiz
            return redirect(reverse('listar_material', args=[idCurso, unidad]))
    else:
        form = VideoForm()
    return render(request, 'crear_video.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})
# editar video
def editar_video(request, id):
    video = Video.objects.get(id=id)
    idCurso = video.curso_id
    unidad = video.unidad_id
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video.titulo = form.cleaned_data['titulo']
            video.link = form.cleaned_data['link']
            video.descripcion = form.cleaned_data['descripcion']
            video.save()
            return redirect(reverse('listar_material', args=[idCurso, unidad]))
    else:
        form = VideoForm(initial={'titulo': video.titulo, 'link': video.link, 'descripcion': video.descripcion})
    return render(request, 'editar_video.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})
# eliminar video
def eliminar_video(request, id):
    video = Video.objects.get(id=id)
    video.delete()
    return redirect(reverse('listar_material', args=[video.curso_id, video.unidad_id]))


# Actividad: crear, editar, eliminar y listar
def crear_actividad(request, idCurso, unidad):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Actividad y asignar el curso y unidad
            actividad = Actividad(curso_id=idCurso, unidad_id=unidad)
            actividad.titulo = form.cleaned_data['titulo']
            actividad.descripcion = form.cleaned_data['descripcion']
            actividad.save()

            # Redirigir a la página del quiz
            return redirect(reverse('listar_material', args=[idCurso, unidad]))
    else:
        form = ActividadForm()

    return render(request, 'crear_actividad.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})



# editar actividad considerando que se puede editar el titulo, descripción, contenido_texto y preguntas de la actividad



# eliminar actividad
def eliminar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    
    # y eliminar los contenidos y preguntas asociados a la actividad
    actividad.contenidos.all().delete()
    actividad.preguntas.all().delete()
    actividad.delete()

    return redirect(reverse('listar_material', args=[actividad.curso_id, actividad.unidad_id]))

# listar actividad
def listar_actividad(request, id):
    actividad = Actividad.objects.get(id=id)
    # Si en actividad_contenido no hay contenido con id de actividad, entonces no se muestra nada
    if actividad.contenidos.count() == 0:
        actividad_cont = None
        # si hay contenido, entonces se muestra
    else:
        actividad_cont = actividad.contenidos.all()
    # Si en actividad_preguntas no hay preguntas con id de actividad, entonces no se muestra nada
    if actividad.preguntas.count() == 0:
        preguntas_preg = None
        # si hay preguntas, entonces se muestra
    else:
        preguntas_preg = actividad.preguntas.all()
    

    idCurso = actividad.curso_id
    unidad = actividad.unidad_id
    return render(request, 'listar_actividad.html', {'actividad': actividad,'preguntas':preguntas_preg,'contenidos':actividad_cont, 'idCurso': idCurso, 'unidad': unidad})

def create_question2(request, id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():

            # Crear una nueva instancia de Question sin ningun parametro
            question = Question()
            question.question_type = form.cleaned_data['question_type']
            question.text = form.cleaned_data['text']
            question.option_a = form.cleaned_data['option_a']
            question.option_b = form.cleaned_data['option_b']
            question.option_c = form.cleaned_data['option_c']
            question.option_d = form.cleaned_data['option_d']
            question.correct_answer = form.cleaned_data['correct_answer']
            question.save()
            # Obtener la instancia de la actividad
            actividad = Actividad.objects.get(id=id)
            # Agregar la pregunta a la lista de preguntas de la actividad
            actividad.preguntas.add(question)

            # Redirigir a la página del listar actividades
            return redirect(reverse('listar_actividad', args=[id]))

    else:
        form = QuestionForm()
    return render(request, 'crear_pregunta.html', {'form': form, 'id': id})


def crear_texto2(request, id):
    
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Contenido y asignar el curso y unidad
            actividad = Actividad.objects.get(id=id)
            contenido = Contenido()
            
            contenido.titulo = form.cleaned_data['titulo']
            contenido.texto = form.cleaned_data['texto']
            contenido.unidad_id = actividad.unidad_id
            contenido.curso_id = actividad.curso_id
            contenido.save()
            
            
            # Agregar el contenido a la lista de contenidos de la actividad
            actividad.contenidos.add(contenido)

            # Redirigir a la página de listar actividad
            return redirect(reverse('listar_actividad', args=[id]))
    else:
        form = TextForm()

    return render(request, 'crear_texto2.html', {'form': form, 'id': id})
# Respuesta Usuario

@login_required 
def formulario(request, idCurso, unidad):
    # Obtener todas las preguntas
    questions = Question.objects.filter(curso_id=idCurso, unidad_id=unidad)
    if request.method == 'POST':
        
        for pregunta in questions:
            question_id = request.POST.get(f'question_id_{pregunta.id}')
            text_answer = request.POST.get(f'text_answer_{pregunta.id}')
            option_answer = request.POST.get(f'option_answer_{pregunta.id}')
            # if form.is_valid():
            # Guardar la respuesta
            answer = Answer()
            # answer question es id de la pregunta
            answer.question = Question.objects.get(id=question_id)
            # answer user es el usuario que esta respondiendo la pregunta
            answer.user = request.user
            answer.text_answer = text_answer
            # answer option_answer es la opcion que el usuario selecciono, puede ser null
            # si es nulo y por lo tanto diferente de a, b, c, d, entonces no se guarda
            if option_answer in ['a', 'b', 'c', 'd']:
                answer.option_answer = option_answer

            answer.save()



        return redirect('agradecimientos')
    else:
        form = AnswerForm()

    return render(request, 'formulario.html', {'form': form, 'questions': questions})



# def agradecimientos, este tendra un mensaje de agradecimiento por haber respondido la encuesta
def agradecimientos(request):
    return render(request, 'agradecimientos.html')










""""
Por el momento no uso listar todas las preguntas
def preguntas(request):
    questions = Question.objects.all()
    return render(request, 'preguntas.html', {'questions': questions})
      """