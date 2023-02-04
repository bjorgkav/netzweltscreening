from django.urls import path, include
from . import views
from home import views as homeviews

app_name = "account" #required for redirects to other apps

urlpatterns = [
    path("login/", views.login, name="login"),
    path("home/index", homeviews.index, name = "index"),
]