from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    #if logged in, redirect to home
    #if not, redirect to login
    template = loader.get_template('index.html') #will automatically look for 'templates' folder
    return HttpResponse(template.render())