from django.shortcuts import render
from transactions.models import Transactions
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from transactions.forms import TransactionsForm

""" 
Este arquivo é responsável por criar as views para listar, inserir, detalhar, atualizar e deletar registros do banco de dados

"""

class NewTransactionCreateView(CreateView):
    model = Transactions
    form_class = TransactionsForm
    template_name = 'new_transaction.html'
