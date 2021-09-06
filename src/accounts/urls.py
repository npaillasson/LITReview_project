from django.urls import path
from .views import new_account, auth

urlpatterns = [
    path('new_account/', new_account, name='new_account'),
    path('auth/', auth, name='auth'),
]