from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewTicketForm
from django.contrib.auth.models import User
from .forms import NewTicketForm

def index(request):
    return render(request, 'review/index.html')

def new_ticket(request):

    user = User.objects.first()
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = user
            ticket.save()
            return redirect('review:index')
    else:
        form = NewTicketForm
    return render(request, 'review/new_ticket.html', {'form': form, 'page': request.path})



