from django.urls import path, include
from . import views
from account import views as accviews

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="homeindex"),
]