from django.urls import path
from . import views
from account import views as accviews


urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="homeindex"),
    path("account/login", accviews.login, name="login")
]