from django.shortcuts import render
from cards.models import Card
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from cards.forms import CardModelForm

""" 
Este arquivo é responsável por criar as views para listar, inserir, detalhar, atualizar e deletar registros do banco de dados

"""

class NewCardCreateView(CreateView):
    model = Card
    form_class = CardModelForm
    template_name = 'new_card.html'
    
    