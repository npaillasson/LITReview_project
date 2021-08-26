from django.urls import path
from .views import index, new_ticket, new_account, auth

urlpatterns = [
    path('', index, name='index'),
    path('new_ticket/', new_ticket, name='new_ticket'),
    path('new_account/', new_account, name='new_account'),
    path('auth/', auth, name='auth'),
]

