from django.shortcuts import render, get_object_or_404

def index(request):
    print(request.user.is_authenticated)
    return render(request, 'review/index.html')

def new_ticket(request):
    print(request.POST)
    return render(request, 'review/new_ticket.html')

