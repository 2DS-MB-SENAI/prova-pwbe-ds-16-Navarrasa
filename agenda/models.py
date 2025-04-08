from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateTimeField()
    cliente_nome = models.CharField(max_length=100)
    cliente_email = models.EmailField()

    def __str__(self):
        return f"{self.servico.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"
    
