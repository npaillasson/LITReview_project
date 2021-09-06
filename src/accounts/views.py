from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

def new_account(request):
    form = UserCreationForm
    return render(request, 'accounts/new_account.html', {'form': form})

def auth(request):
    return render(request, 'accounts/auth.html')
