from django.urls import path
from .views import RealHome

app_name = "realisations"

urlpatterns = [
    path('realisations/', RealHome.as_view(), name="home"),

]