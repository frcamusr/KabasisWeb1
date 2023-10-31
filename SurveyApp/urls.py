from django.urls import path
from . import views

urlpatterns = [
    # crear pregunta usando el camino /create_question/'idCurso'/'unidad'/ usando la vista create_question en la app SurveyApp
    path('crear_pregunta/<int:idCurso>/<int:unidad>/', views.create_question, name='crear_pregunta'),
    path('preguntas/', views.preguntas, name='preguntas'),
    # formulario con idCurso y unidad como parametros
    path('formulario/<int:idCurso>/<int:unidad>/', views.formulario, name='formulario'),

    path('agradecimientos/', views.agradecimientos, name='agradecimientos'),
    # delete_question
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    # actualizar pregunta usando el mismo formulario de crear pregunta
    path('update_question/<int:id>/', views.update_question, name='update_question'),    
    # quiz
    path('quiz/<int:idCurso>/<int:unidad>/', views.quiz, name='quiz')
]

