from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def index(request):
    #get request data and display
    territories = request.get("https://netzwelt-devtest.azurewebsites.net/Territories/All")
    print(territories.text)
    return render(request, 'index.html', {})