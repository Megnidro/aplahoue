from django.urls import path
from .views import ValeurHome

app_name = "valeurs"

urlpatterns = [
    path('', ValeurHome.as_view(), name="home"),

]