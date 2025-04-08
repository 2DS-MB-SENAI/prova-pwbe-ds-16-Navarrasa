from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServicosSerializer, AgendamentoSerializer
from .models import Servico, Agendamento


"""
    Serviços, Agendamentos
   
    Função para listar todos os serviços cadastrados no sistema.

    -> Obtém todos os serviços do banco de dados do banco de dados e os transforma em json.
    -> O serializer é usado para converter os dados do modelo Servicos em JSON.
    -> Se o método da requisição for GET, retorna todos os serviços.
    -> Se o método for POST, cria um novo serviço com os dados fornecidos na requisição.
    -> Se os dados do serviço forem válidos, salva o novo serviço no banco de dados.

"""
@api_view(['GET', 'POST'])
def listar_servicos(request):
    if request.method == 'GET':
        serializer = ServicosSerializer(Servico.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ServicosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def detalhes_servico(request, pk):
    try:
        servico = Servico.objects.get(pk=pk)
        serializer = ServicosSerializer(servico)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Servico.DoesNotExist:
        return Response({"detail": "Serviço não encontrado."}, status=status.HTTP_404_NOT_FOUND)


# Agendamentos
def listar_agendamentos(request):

    # Função para listar todos os agendamentos cadastrados no sistema.
    # Obtém todos os agendamentos do banco de dados e os transforma em json.
    # O serializer é usado para converter os dados do modelo Agendamento em JSON.
    # Se o método da requisição for GET, retorna todos os agendamentos.
    # Se o método for POST, cria um novo agendamento com os dados fornecidos na requisição.

    if request.method == 'GET':
        serializer = AgendamentoSerializer(Agendamento.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def detalhes_agendamento(request, pk):
    try:

        # Obtém o agendamento com o ID fornecido
        # e retorna os detalhes do agendamento em formato JSON.

        agendamento = Agendamento.objects.get(pk=pk)
        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Agendamento.DoesNotExist:
        return Response({"detail": "Agendamento não encontrado."}, status=status.HTTP_404_NOT_FOUND)