from django.contrib import admin
from django.urls import path
from cards.views import NewCardCreateView
from transactions.views import NewTransactionCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_card/', NewCardCreateView.as_view(), name='new_card'),
    path('new_transactions/', NewTransactionCreateView.as_view(), name='transactions')
]
