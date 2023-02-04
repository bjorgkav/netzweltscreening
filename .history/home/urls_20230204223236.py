from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("index/", views.index, name="homeindex"),
]