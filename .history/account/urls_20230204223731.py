from django.urls import path, include
from . import views

app_name = "account" #required for redirects, adding namespaces to project URLS

urlpatterns = [
    path("login/", views.login, name="login"),
]