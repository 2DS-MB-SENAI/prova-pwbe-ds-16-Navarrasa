from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

"""
    Função para registrar novos usuários no sistema.
    -> O serializer é usado para converter os dados do modelo CustomUser em JSON.
    -> Se o método da requisição for POST, cria um novo usuário com os dados fornecidos na requisição.
    -> Se os dados do usuário forem válidos, salva o novo usuário no banco de dados.
    -> Se o método não for POST, retorna um erro de método não permitido.
    -> O serializer é usado para converter os dados do modelo CustomUser em JSON.

"""
@api_view(['POST'])
def registro_usuarios(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """
    Função para exibir o perfil do usuário autenticado.
    -> Obtém os dados do usuário autenticado e os passa para o template 'user_profile.html'.
    -> O template exibe informações sobre o usuário, como nome, e-mail e data de registro.
    """
    if request.user.is_authenticated:
        user = request.user
        context = {
            'user': user,
        }
        return render(request, 'user_profile.html', context)
    else:
        return Response({"detail": "Usuário não autenticado."}, status=status.HTTP_401_UNAUTHORIZED)