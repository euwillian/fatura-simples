from django.db import models
from cards.models import Card

"""
Transações

Data
Valor total
Parcelas
Descrição
Quem gastou

"""

class Transactions(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.PROTECT, related_name='fk_card_name')
    expense_date = models.DateField(blank=False, null=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    number_installments = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True, max_length=240)
    who_spent = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.description} - {self.total_amount}"

    