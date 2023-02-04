from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path("", views.redirect_index, name="index"),
    path("index/", views.index, name="homeindex"),
]