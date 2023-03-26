# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def services(request):
    return render(request, 'home/services.html')
