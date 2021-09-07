from django.urls import path
from .views import index, new_ticket, subscription_page

urlpatterns = [
    path('', index, name='index'),
    path('new_ticket/', new_ticket, name='new_ticket'),
    path('ticket_change/', new_ticket, name='ticket_change'),
    path('subscription/', subscription_page, name='subscription_page')
]

