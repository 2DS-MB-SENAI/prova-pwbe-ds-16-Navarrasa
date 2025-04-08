from .views import listar_servicos, detalhes_servico, listar_agendamentos, detalhes_agendamento
from django.urls import path

urlpatterns = [
    # EndPoints sobre serviços
    path('api/servicos/', listar_servicos, name='listar_servicos'),
    path('api/servicos/<int:pk>', detalhes_servico, name='detalhes_servico'),

    # EndPoints sobre agendamentos
    path('api/agendamentos/', listar_agendamentos, name='listar_agendamentos'),
    path('api/agendamentos/<int:pk>/', detalhes_agendamento, name='detalhes_agendamento'),
]
