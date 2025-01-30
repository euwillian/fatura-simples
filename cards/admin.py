from django.contrib import admin
from cards.models import Card

"""

Este arquivo é responsável por mostrar as tabelas no /admin

"""


class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'due_date', 'payment_date')
    search_fields = ('card_name',)

admin.site.register(Card, CardAdmin)