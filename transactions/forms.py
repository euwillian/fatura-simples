from django import forms
from transactions.models import Transactions

""" 
Este arquivo é responsável por criar o formulário em tela com todos os campos do Models.py

"""

class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'
        labels = {
            'card_id': 'Cartão',
            'expense_date': 'Data',
            'total_amount': 'Total',
            'number_installments': 'Parcelas',
            'description': 'Descrição',
            'who_spent': 'Quem gastou?'
        }
        
    # abaixo colocar as validações dos campos, regras etc.