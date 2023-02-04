from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    #if logged in, redirect to home
    #if not, redirect to login
    return redirect(request, "/login.html", {})