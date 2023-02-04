from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="homeindex"),
]