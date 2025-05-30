# Generated by Django 4.2 on 2025-04-08 12:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('crm', models.CharField(help_text='Formato: XX/XXXXX (ex: SP/12345)', max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='O CRM deve estar no formato XX/XXXXX (ex: SP/12345)', regex='^[A-Z]{2}/\\d{5}$')])),
                ('especialidade', models.CharField(choices=[('clinico', 'Clínico Geral'), ('cardiologista', 'Cardiologista'), ('dermatologista', 'Dermatologista'), ('pediatra', 'Pediatra'), ('ortopedista', 'Ortopedista')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=100)),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('agendado', 'Agendado'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], max_length=20)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
