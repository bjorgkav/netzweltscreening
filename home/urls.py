from django.urls import path, include
from . import views

app_name = "home" #required for redirects, adding namespaces to project URLS

urlpatterns = [
    path("", views.redirect_index, name="default"),
    path("index/", views.index, name="index"),
]