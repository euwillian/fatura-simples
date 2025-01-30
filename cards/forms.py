from django import forms
from cards.models import Card

""" 
Este arquivo é responsável por criar o formulário em tela com todos os campos do Models

"""

class CardModelForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
    
    # abaixo validações de cada campo