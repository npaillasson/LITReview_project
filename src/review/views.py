from django.shortcuts import render

def index(request):
    print(request.user.is_authenticated)
    return render(request, 'review/index.html')
