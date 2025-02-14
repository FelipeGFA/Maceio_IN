from django.db import models

class Pessoa(models.Model):
    SETORES = (
        ('contabilidade', 'Contabilidade'),
        ('financeiro', 'Financeiro'),
        ('atendimento', 'Atendimento'),
        ('orcamento', 'Orçamento'),
        ('ti', 'TI'),
    )

    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=20, choices=SETORES)
    email = models.EmailField()

    def __str__(self):
        return self.nome
