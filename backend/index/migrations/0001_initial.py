# Generated by Django 5.1.6 on 2025-02-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('setor', models.CharField(choices=[('contabilidade', 'Contabilidade'), ('financeiro', 'Financeiro'), ('atendimento', 'Atendimento'), ('orcamento', 'Orçamento'), ('ti', 'TI')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
