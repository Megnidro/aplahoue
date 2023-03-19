from django.shortcuts import render
from django.views.generic import ListView


from .models import RealisationPost


class RealHome(ListView):
    model = RealisationPost
    context_object_name = "posts"
    template_name = "realisations/list.html"
    paginate_by = 3
