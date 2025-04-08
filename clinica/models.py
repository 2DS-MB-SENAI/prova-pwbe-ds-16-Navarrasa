from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

"""
Model Médicos:

-> Cria um modelo para armazenar informações sobre médicos, incluindo nome, especialidade, CRM e e-mail.
-> O modelo inclui um método __str__ para retornar o nome do médico como representação legível.

"""


# Validador para o formato XX/XXXXX
"""
O RegexValidator usa a expressão regular ^\d{2}/\d{5}$:
^\d{2}: Começa com exatamente 2 números inteiros 1-9
/: Seguido de uma barra
\d{5}$: Termina com exatamente 5 dígitos
:https://docs.djangoproject.com/en/5.2/ref/validators/#regexvalidator

"""

crm_validator = RegexValidator(
    regex=r'^\d{2}/\d{5}$',
    message='O CRM deve estar no formato XX/XXXXX (ex: 11/12345)',
)


class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(
        max_length=8,
        unique=True,
        validators=[crm_validator],
        help_text="Formato: XX/XXXXX (ex: 11/12345)"
    )
    especialidade = models.CharField(max_length=100, choices=[
        ('clinico', 'Clínico Geral'),
        ('cardiologista', 'Cardiologista'),
        ('dermatologista', 'Dermatologista'),
        ('pediatra', 'Pediatra'),
        ('ortopedista', 'Ortopedista'),
        ('CAR', 'Cardiologista')
    ])
    email = models.EmailField(max_length=100, unique=False, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.crm}"

"""
Model Consultas:

-> Cria um modelo para armazenar informações sobre consultas, incluindo paciente, data, médico e status.
-> O status da consulta pode ser agendado, realizado ou cancelado.
-> O modelo inclui um método __str__ para retornar uma representação legível da consulta.

"""

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ])

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico.nome} em {self.data}"
    