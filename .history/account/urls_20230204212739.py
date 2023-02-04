from django.urls import path
from . import views
from django.urls import include, path


urlpatterns = [
    path("login/", views.login, name="login"),
    path("home/index", homeviews.index, name="index"),
]