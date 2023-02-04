from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def simplify(list):
    simplified = {}

    for dict in list:
        print(dict["name"])
    return simplified

def index(request):
    #get request data and display
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All").json()["data"] #list of dictionaries
    
    simplified_t = simplify(territories)

    print(territories[0]["name"])
    print(territories)
    print(simplified_t)

    return render(request, 'index.html', {})