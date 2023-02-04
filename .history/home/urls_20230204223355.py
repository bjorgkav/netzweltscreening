from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path("", views.redirect_index, name="blank"),
    path("index/", views.index, name="index"),
]