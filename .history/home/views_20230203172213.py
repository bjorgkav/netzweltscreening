from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def index(request):
    #get request data and display
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All").json()["data"] #list of dictionaries
    #print(f"{territories.json()}, {type(territories.json())}")
    processed_territories = {}
    for t  in territories:
        if processed_territories[t["name"]] not in processed_territories:
            processed_territories[t["name"]] = ""
    #print(sorted(territories, key=lambda d:d["id"]))
    return render(request, 'index.html', {})