from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
#  Validar se a data passada pelo usuário é maior que a data atual
def validate_past_date(value):
    if value and value > timezone.now().date():
        raise ValidationError('A data de nascimento deve estar no passado.')

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True, validators=[validate_past_date], help_text="Formato: YYYY-MM-DD (ex: 1990-01-01)")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username