from django.shortcuts import render, get_object_or_404

def new_account(request):
    return render(request, 'accounts/new_account.html')

def auth(request):
    return render(request, 'accounts/auth.html')
