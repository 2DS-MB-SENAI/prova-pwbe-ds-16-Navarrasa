from .views import listar_medicos, criar_consulta, detalhes_consulta
from django.urls import path

urlpatterns = [
    path('medicos/', listar_medicos, name='listar_medicos'),
    path('consultas/nova/', criar_consulta, name='criar_consulta'),
    path('consultas/<int:pk>/', detalhes_consulta, name='detalhes_consulta'),
]
