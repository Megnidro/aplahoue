from django.urls import path
from .views import BlogHome, BlogPostDetail

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),

]