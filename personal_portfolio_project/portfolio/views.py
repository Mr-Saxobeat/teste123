from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def fraude(request):
    return render(request, 'portfolio/home.html')
<<<<<<< HEAD

def agathinha(request):
    return render(request, 'portfolio/agathinha.html')
=======
>>>>>>> 171912b1ad87cf44a656baf5b6edbfb307bc7c67
