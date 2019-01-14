from django.db import models

# Create your models here.
TipoDespesa_choices = {
    ('', (
        ('1', 'Remédio'),
        ('2', 'Roupas'),
        ('3', 'Alimentação'),
        ('4', 'Educação'),
        ('5', 'Transporte'),
        ('6', 'Outros'),
    ),
     ),
}

FormaPagamento_choices = {
    (' ', (
        ('A', 'Dinheiro'),
        ('B', 'Cartão de Crédito'),
        ('C', 'Cartão de Débito'),
        ('D', 'Cartão Crediário'),
        ('E', 'Cheque'),
    ),
     ),
}

class DespesaAna(models.Model):
    data_criacao = models.CharField('Data Criação', max_length=10)
    tipo_despesa = models.CharField('Tipo do Gasto', max_length=100, choices = TipoDespesa_choices, default=' ')
    descricao = models.TextField('Descrição')
    forma_pagamento = models.CharField('Forma Pagamento', max_length=50, choices = FormaPagamento_choices, default=' ')
    vencimento = models.DateField('Vencimento')
    quitado = models.BooleanField('Quitado')

    class Meta:
        ordering = ('vencimento', '-forma_pagamento')
