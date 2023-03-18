from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import ValeurPost


class ValeurHome(ListView):
    model = ValeurPost
    context_object_name = "posts"
    template_name = "valeurs/list.html"
