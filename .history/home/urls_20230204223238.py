from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="homeindex"),
]