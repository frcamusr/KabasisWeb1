from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import QuestionForm, AnswerForm, ContenidoForm
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
            return redirect(reverse('quiz', args=[id]))
    else:
        form = QuestionForm()
    return render(request, 'crear_pregunta.html', {'form': form, 'id_quiz': id})


def delete_question(request, id):
    question = Question.objects.get(quiz_id=id)

    question.delete()
    return redirect(reverse('quiz', args=[id]))


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
                return redirect(reverse('quiz', args=[id]))

            else:
                #form = QuestionForm(initial={'text': question.text, 'option_a': question.option_a, 'option_b': question.option_b, 'option_c': question.option_c, 'option_d': question.option_d, 'correct_answer': question.correct_answer})

                question.text = form.cleaned_data['text']
                question.option_a = form.cleaned_data['option_a']
                question.option_b = form.cleaned_data['option_b']
                question.option_c = form.cleaned_data['option_c']
                question.option_d = form.cleaned_data['option_d']
                question.correct_answer = form.cleaned_data['correct_answer']
                question.save()
                return redirect(reverse('quiz', args=[id]))
        else:
            if tipo == 'text':
                form = QuestionForm(initial={'text': question.text})
            else:
                form = QuestionForm(initial={'text': question.text, 'option_a': question.option_a, 'option_b': question.option_b, 'option_c': question.option_c, 'option_d': question.option_d, 'correct_answer': question.correct_answer})
        
   
    return render(request, 'update_question.html', {'form': form, 'question': question, 'tipo': tipo})


#Quiz: crear, editar y eliminar

def crear_quiz(request, idCurso, unidad):
    # creamos el quiz sin formulario directamente en la vista usando el modelo Quiz y idCurso y unidad como parametros
    quiz = Quiz()
    quiz.curso_id = idCurso
    quiz.unidad_id = unidad
    quiz.save()
    # redireccionamos a listar_quiz
    return redirect(reverse('listar_quiz', args=[idCurso, unidad]))

    

def edit_quiz_p(request, id):
    quiz = Quiz.objects.get(id=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Guardar la pregunta y sus opciones
            question = Question()

            question.quiz_id = quiz.id
            question.curso_id = quiz.curso_id
            question.unidad_id = quiz.unidad_id
            question.question_type = form.cleaned_data['question_type']
            question.text = form.cleaned_data['text']
            question.option_a = form.cleaned_data['option_a']
            question.option_b = form.cleaned_data['option_b']
            question.option_c = form.cleaned_data['option_c']
            question.option_d = form.cleaned_data['option_d']
            question.correct_answer = form.cleaned_data['correct_answer']
            question.save()
        return redirect('quiz')
    else:
        form = QuestionForm()
    return render(request, 'crear_pregunta.html', {'form': form, 'quiz': quiz})

# edit_quiz solo envia a la lista de quiz
def edit_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    idCurso = quiz.curso_id
    unidad = quiz.unidad_id
    return redirect(reverse('quiz', args=[quiz.id]))

# Eliminar quiz y sus preguntas
def delete_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    quiz.delete()
    return redirect(reverse('listar_quiz', args=[quiz.curso_id, quiz.unidad_id]))



def quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    idCurso = quiz.curso_id
    unidad = quiz.unidad_id
    questions = Question.objects.filter(quiz_id=id)
    return render(request, 'quiz.html', {'questions': questions, 'quiz':quiz ,'idCurso': idCurso, 'unidad': unidad})




def ver_quiz(request, id_quiz):
    # Ver el quiz con el id_quiz
    quiz = Quiz.objects.get(id=id_quiz)
    return render(request, 'quiz.html', {'quiz': quiz})



# mostrar los enlaces de todos los quiz creados para cada unidad y curso:
def listar_material(request, idCurso, unidad):
    quizzes = Quiz.objects.filter(curso_id=idCurso, unidad_id=unidad)
    idCurso = idCurso
    unidad = unidad

    if not quizzes:
        mensaje = "No existen quizzes para este curso y unidad."
        return render(request, 'listar_quiz.html', {'mensaje': mensaje, 'idCurso': idCurso, 'unidad': unidad})

    return render(request, 'listar_material.html', {'quizzes': quizzes, 'idCurso': idCurso, 'unidad': unidad})



def listar_contenido(request, idCurso, unidad):
    contenido = Contenido.objects.filter(curso_id=idCurso, unidad_id=unidad)
    return render(request, 'listar_contenido.html', {'contenido': contenido, 'idCurso': idCurso, 'unidad': unidad})

def crear_contenido(request, idCurso, unidad):
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            # Guardar el contenido
            contenido = Contenido()
            contenido.titulo = form.cleaned_data['titulo']
            contenido.contenido = form.cleaned_data['contenido']
            contenido.curso_id = idCurso
            contenido.unidad_id = unidad
            contenido.save()
        return redirect(reverse('listar_contenido', args=[idCurso, unidad]))
    else:
        form = ContenidoForm()
    return render(request, 'crear_contenido.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})






def listar_videos(request, idCurso, unidad):
    videos = Video.objects.filter(curso_id=idCurso, unidad_id=unidad)
    return render(request, 'listar_videos.html', {'videos': videos, 'idCurso': idCurso, 'unidad': unidad})

def crear_video(request, idCurso, unidad):
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            # Guardar el contenido
            video = Video()
            video.link = form.cleaned_data['titulo']
            video.descripcion = form.cleaned_data['contenido']
            video.curso_id = idCurso
            video.unidad_id = unidad
            video.save()
        return redirect(reverse('listar_videos', args=[idCurso, unidad]))
    else:
        form = ContenidoForm()
    return render(request, 'crear_video.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})





def listar_actividad(request, idCurso, unidad):
    actividades = Actividad.objects.filter(curso_id=idCurso, unidad_id=unidad)
    return render(request, 'listar_actividad.html', {'actividades': actividades, 'idCurso': idCurso, 'unidad': unidad})

def crear_actividad(request, idCurso, unidad):
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            # Guardar el contenido
            actividad = Actividad()
            actividad.titulo = form.cleaned_data['titulo']
            actividad.contenido = form.cleaned_data['contenido']
            actividad.curso_id = idCurso
            actividad.unidad_id = unidad
            actividad.save()
        return redirect(reverse('listar_actividades', args=[idCurso, unidad]))
    else:
        form = ContenidoForm()
    return render(request, 'crear_actividad.html', {'form': form, 'idCurso': idCurso, 'unidad': unidad})





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