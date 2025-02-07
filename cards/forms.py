from django import forms
from cards.models import Card

""" 
Este arquivo é responsável por criar o formulário em tela com todos os campos do Models.py

"""

class CardModelForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        labels = {
            'card_name': 'Cartão',
            'due_date': 'Dia Vencimento',
            'payment_date': 'Dia Pagamento',
        }
    
    # abaixo validações de cada campo