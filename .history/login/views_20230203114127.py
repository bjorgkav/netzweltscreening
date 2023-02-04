from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #if logged in, redirect to home
    #if not, redirect to login
    return HttpResponse("This is an HTTP Response.")