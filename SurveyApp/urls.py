from django.urls import path
from . import views

urlpatterns = [

    # por el momento no uso este url:path('preguntas/', views.preguntas, name='preguntas'),


    # URL para Pregunta
    # crear pregunta solo usando el id del quiz
    path('crear_pregunta/<int:id>/', views.create_question, name='crear_pregunta'),  
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    # actualizar pregunta usando el mismo formulario de crear pregunta
    path('update_question/<int:id>/', views.update_question, name='update_question'),    
    # quiz con id como parametro
    path('quiz/<int:id>/', views.quiz, name='quiz'),



    # URL para Quiz
    # path para editar quiz
    path('editar_quiz/<int:id>/', views.edit_quiz, name='editar_quiz'),
    # path para eliminar quiz
    path('eliminar_quiz/<int:id>/', views.delete_quiz, name='eliminar_quiz'),
    # path para crear_quiz
    path('crear_quiz/<int:idCurso>/<int:unidad>/', views.crear_quiz, name='crear_quiz'),


    # URL para Contenido
    # path para crear contenido
    path('crear_contenido/<int:idCurso>/<int:unidad>/', views.crear_contenido, name='crear_contenido'),
    # path para editar contenido
    path('editar_contenido/<int:id>/', views.edit_contenido, name='editar_contenido'),
    # path para eliminar contenido
    path('eliminar_contenido/<int:id>/', views.delete_contenido, name='eliminar_contenido'),

    # URL para Video
    # path para crear video
    path('crear_video/<int:idCurso>/<int:unidad>/', views.crear_video, name='crear_video'),
    # path para editar video
    path('editar_video/<int:id>/', views.edit_video, name='editar_video'),
    # path para eliminar video
    path('eliminar_video/<int:id>/', views.delete_video, name='eliminar_video'),

    # URL para Actividad
    # path para crear actividad
    path('crear_actividad/<int:idCurso>/<int:unidad>/', views.crear_actividad, name='crear_actividad'),
    # path para editar actividad
    path('editar_actividad/<int:id>/', views.edit_actividad, name='editar_actividad'),
    # path para eliminar actividad
    path('eliminar_actividad/<int:id>/', views.delete_actividad, name='eliminar_actividad'),





  
    # Responder Usuario
    # formulario y agradecimientos
    path('formulario/<int:idCurso>/<int:unidad>/', views.formulario, name='formulario'),
    path('agradecimientos/', views.agradecimientos, name='agradecimientos'),







    #  path para listar contenido
    path('listar_material/<int:idCurso>/<int:unidad>/', views.listar_material, name='listar_material'),










]

