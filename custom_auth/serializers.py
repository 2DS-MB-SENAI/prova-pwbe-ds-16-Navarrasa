from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Inclui todos os campos do modelo
        # fields = ['username', 'email', 'password']  # Inclui apenas os campos desejados
        extra_kwargs = {'password': {'write_only': True}}  # Define o campo de senha como somente para escrita
