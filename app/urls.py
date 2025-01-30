from django.contrib import admin
from django.urls import path
from cards.views import NewCardCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_card/', NewCardCreateView.as_view(), name='new_card'),
    #path('transactions/', name='transactions')
]
