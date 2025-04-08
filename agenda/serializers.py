from rest_framework import serializers
from .models import Servico, Agendamento


class ServicosSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Servicos.
    Este serializer é usado para converter instâncias do modelo Servicos em formatos JSON e vice-versa.
    """
    class Meta:
        model = Servico
        fields = '__all__'  # Inclui todos os campos do modelo

class AgendamentoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Agendamento.
    Este serializer é usado para converter instâncias do modelo Agendamento em formatos JSON e vice-versa.
    """
    class Meta:
        model = Agendamento
        fields = '__all__'  # Inclui todos os campos do modelo

