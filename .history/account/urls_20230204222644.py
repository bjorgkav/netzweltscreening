from django.urls import path, include
from . import views
from home import views as homeviews

urlpatterns = [
    path("login/", views.login, name="login"),
]