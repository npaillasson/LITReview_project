from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


def new_account(request):
    if request.user.is_authenticated:
        return redirect('review:index')
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('review:index')
    else:
        form = UserCreationForm
    return render(request, 'accounts/new_account.html', {'form': form})
