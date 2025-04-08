from django.shortcuts import render
from .models import Medico, Consulta
from .forms import ConsultaForm
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

def listar_medicos(request):
    """
    Função para listar todos os médicos cadastrados no sistema.

    -> Obtém todos os médicos do banco de dados e os passa para o template 'listar_medicos.html'.
    -> O template exibe uma tabela com informações sobre cada médico, incluindo nome, especialidade, CRM e e-mail.

    """
    medicos = get_object_or_404(Medico.objects.all())
    # Aplicando o filtro de médicos
    # filtro = MedicoFilter(request.GET, queryset=medicos)
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    """
    Função para criar uma nova consulta.

    -> Se o método da requisição for POST, obtém os dados do formulário e cria uma nova consulta.
    -> Se o método for GET, exibe o formulário para criar uma nova consulta.
    -> O formulário inclui campos para selecionar o paciente, a data da consulta e o médico responsável.
    -> O médico é selecionado a partir de uma lista de médicos cadastrados no sistema.
    
    """
    
    try:
        if request.method == 'POST':
            form = ConsultaForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'clinica/sucesso.html', {'mensagem': 'Consulta criada com sucesso!'})
        else:
            form = ConsultaForm()

        medicos = Medico.objects.all()
        return render(request, 'clinica/form_consulta.html', {'form': form, 'medicos': medicos})
    except Exception as e:
        return render(request, 'clinica/erro.html', {'mensagem': str(e)})

def detalhes_consulta(request, pk):
    """
    Função para exibir os detalhes de uma consulta específica.
    
    -> Obtém a consulta com o ID fornecido e passa os detalhes para o template 'detalhes_consulta.html'.
    -> O template exibe informações detalhadas sobre a consulta, incluindo paciente, data, médico e status.
    -> O ID da consulta é passado como parâmetro na URL e utilizado para buscar a consulta no banco de dados.
    -> O método get() é utilizado para buscar a consulta com o ID fornecido.
    -> Caso a consulta não seja encontrada, uma exceção será lançada.

    """

    try:

        consulta = Consulta.objects.get(id=pk)
        return render(request, 'clinica/detalhes_consulta.html', {'consulta': consulta})
    
    except Consulta.DoesNotExist:
        return render(request, 'clinica/erro.html', {'mensagem': 'Consulta não encontrada.'})