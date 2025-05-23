# Generated by Django 4.2 on 2025-04-08 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_medico_email_alter_consulta_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.CharField(help_text='Formato: XX/XXXXX (ex: SP/12345)', max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='O CRM deve estar no formato XX/XXXXX (ex: SP/12345)', regex='^[d]{2}/\\d{5}$')]),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(choices=[('clinico', 'Clínico Geral'), ('cardiologista', 'Cardiologista'), ('dermatologista', 'Dermatologista'), ('pediatra', 'Pediatra'), ('ortopedista', 'Ortopedista'), ('CAR', 'Cardiologista')], max_length=100),
        ),
    ]
