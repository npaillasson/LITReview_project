from django.urls import path
from django.contrib.auth import views as auth_views

from .views import new_account, auth

urlpatterns = [
    path('new_account/', new_account, name='new_account'),
    path('auth/', auth, name='auth'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]