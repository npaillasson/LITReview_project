from django.urls import path
from .views import index, new_ticket

urlpatterns = [
    path('', index, name='index'),
    path('new_ticket/', new_ticket, name='new_ticket'),
]

