import django_filters
from .models import Medico

"""
FilterSet para o modelo Medico:
-> Permite filtrar médicos com base em critérios como nome e especialidade.
-> O filtro de nome utiliza uma busca insensível a maiúsculas e minúsculas (icontains).

"""

class MedicoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    especialidade = django_filters.ChoiceFilter(choices=[
        ('cardiologia', 'Cardiologia'),
        ('dermatologia', 'Dermatologia'),
        ('pediatria', 'Pediatria'),
        ('ortopedia', 'Ortopedia'),
        ('neurologia', 'Neurologia'),
    ])

    class Meta:
        model = Medico
        fields = ['nome', 'especialidade']