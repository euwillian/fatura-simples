from django.contrib import admin
from transactions.models import Transactions

"""

Este arquivo é responsável por mostrar as tabelas no /admin

"""

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'expense_date', 'total_amount', 'number_installments', 'description', 'who_spent', 'created_at')
    search_fields = ('description', 'expense_date',)

admin.site.register(Transactions, TransactionsAdmin)
