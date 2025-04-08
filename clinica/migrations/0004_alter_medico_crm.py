# Generated by Django 4.2 on 2025-04-08 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0003_alter_medico_crm_alter_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.CharField(help_text='Formato: XX/XXXXX (ex: 11/12345)', max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='O CRM deve estar no formato XX/XXXXX (ex: 11/12345)', regex='^d{2}/\\d{5}$')]),
        ),
    ]
