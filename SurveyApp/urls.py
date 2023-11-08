from django.urls import path
from . import views

urlpatterns = [

    # por el momento no uso este url:path('preguntas/', views.preguntas, name='preguntas'),


    # URL para Pregunta
    # crear pregunta solo usando el id del quiz
    path('crear_pregunta/<int:id>/', views.create_question, name='crear_pregunta'),  
    #crear pregunta usando la vista create_question2 y enviando el id de la actividad
    path('crear_pregunta2/<int:id>/', views.create_question2, name='crear_pregunta2'),


    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    # actualizar pregunta usando el mismo formulario de crear pregunta
    path('update_question/<int:id>/', views.update_question, name='update_question'),    




    # URL para Quiz
    # path para crear_quiz
    path('crear_quiz/<int:idCurso>/<int:unidad>/', views.crear_quiz, name='crear_quiz'),
    # path para editar quiz
    path('editar_quiz/<int:id>/', views.edit_quiz, name='editar_quiz'),
    # path para eliminar quiz
    path('eliminar_quiz/<int:id>/', views.delete_quiz, name='eliminar_quiz'),
    # quiz con id como parametro para listar las preguntas
    path('listar_quiz/<int:id>/', views.listar_quiz, name='listar_quiz'),


    # URL para texto
    # path para crear contenido
    path('crear_texto/<int:idCurso>/<int:unidad>/', views.crear_texto, name='crear_texto'),
    # path para vista crear_texto2
    path('crear_texto2/<int:id>/', views.crear_texto2, name='crear_texto2'),


    
    # path para editar contenido
    path('editar_texto/<int:id>/', views.editar_texto, name='editar_texto'),
    # path para eliminar contenido
    path('eliminar_texto/<int:id>/', views.eliminar_texto, name='eliminar_texto'),

    # URL para Video
    # path para crear video
    path('crear_video/<int:idCurso>/<int:unidad>/', views.crear_video, name='crear_video'),
    # path para editar video
    path('editar_video/<int:id>/', views.editar_video, name='editar_video'),
    # path para eliminar video
    path('eliminar_video/<int:id>/', views.eliminar_video, name='eliminar_video'),

    # URL para Actividad
    # path para crear actividad
    path('crear_actividad/<int:idCurso>/<int:unidad>/', views.crear_actividad, name='crear_actividad'),
    # path para editar actividad
    # path('editar_actividad/<int:id>/', views.editar_actividad, name='editar_actividad'),
    # path para eliminar actividad
    path('eliminar_actividad/<int:id>/', views.eliminar_actividad, name='eliminar_actividad'),
    # path para listar actividades
    path('listar_actividad/<int:id>/', views.listar_actividad, name='listar_actividad'),

 



  
    # Responder Usuario
    # formulario y agradecimientos
    path('formulario/<int:idCurso>/<int:unidad>/', views.formulario, name='formulario'),
    path('agradecimientos/', views.agradecimientos, name='agradecimientos'),







    #  path para listar todo el material de la unidad
    path('listar_material/<int:idCurso>/<int:unidad>/', views.listar_material, name='listar_material'),










]

