from django.shortcuts import render, get_object_or_404
from .forms import NewTicketForm
from django.contrib.auth.models import User

def index(request):
    print(request.user.is_authenticated)
    return render(request, 'review/index.html')

def new_ticket(request):
    #if request.method == 'POST':
    #    form = NewTicketForm(request.POST)
    print(request.POST)
    print(User.objects.first())
    return render(request, 'review/new_ticket.html')

def new_account(request):
    return render(request, 'review/new_account.html')

