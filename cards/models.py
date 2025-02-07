from django.db import models

"""
Este arquivo é reponsável por criar todo o banco de dados de acordo com os campos

Cartão:
    id
    Nome do cartão
    Dia de vencimento
    Dia de pagamento
"""

class Card(models.Model):
    card_name = models.CharField(max_length=10, blank=False, null=False)
    due_date = models.DateField(blank=False, null=False)  # dia vencimento, talvez mudar para varchar ou int
    payment_date = models.DateField(blank=False, null=False) # dia pagamento, talvez mudar para varchar ou int
    
    def __str__(self):
        return self.card_name
    