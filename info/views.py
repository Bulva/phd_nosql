from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def bio(request):
    return render(request, 'bio.html')


def skills(request):
    return render(request, 'skills.html')


def projects(request):
    return render(request, 'projects.html')
