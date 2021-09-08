from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTicketForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewTicketForm, NewFollowedUser

@login_required
def index(request):
    section = "flux"
    return render(request, 'review/index.html', {'page': request.path, 'section': section})

@login_required()
def new_ticket(request):

    if request.method == 'POST':
        form = NewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.image = form.cleaned_data.get('image')
            ticket.user = request.user
            ticket.save()
            return redirect('review:index')
    else:
        form = NewTicketForm
    return render(request, 'review/new_ticket.html', {'form': form, 'page': request.path})

@login_required()
def subscription_page(request):

    section = 'subscription'
    if request.method == 'POST':
        form = NewFollowedUser(request.POST)
        if form.is_valid():
            user_follow = form.save(commit=False)
            user_follow.user = request.user
            user_follow.save()
            return redirect('review:subscription_page')
    else:
        form = NewFollowedUser
    return render(request, 'review/subscriptions.html', {'form': form, 'section': section})



