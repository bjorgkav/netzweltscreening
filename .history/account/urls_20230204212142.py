from django.urls import path
from . import views
from home import views as homeviews

urlpatterns = [
    path("login/", views.login, name="login"),
    path("home/index", )
]