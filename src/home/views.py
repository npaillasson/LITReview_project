from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bonjour est bienvenue sur le site!</h1>')