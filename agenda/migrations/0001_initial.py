# Generated by Django 4.2 on 2025-04-08 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('cliente_nome', models.CharField(max_length=100)),
                ('cliente_email', models.EmailField(max_length=254)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.servico')),
            ],
        ),
    ]
