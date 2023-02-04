from django.urls import path, include
from . import views
from account import views as accviews

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="homeindex"),
    path("account/login", accviews.login, name="login")
]