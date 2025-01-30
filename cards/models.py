from django.db import models

"""
Este arquivo é reponsável por criar todo o banco de dados de acordo com os campos

Cartão:
    id
    Nome do cartão
    Data de vencimento da fatura
    Data de pagamento
"""

class Card(models.Model):
    card_name = models.CharField(max_length=10, blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)
    payment_date = models.DateField(blank=False, null=False)
    
    def __str__(self):
        return self.card_name