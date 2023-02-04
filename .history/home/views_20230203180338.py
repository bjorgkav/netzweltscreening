from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def simplify(list):
    simplified = {}
    for dict in list:
        if dict["name"] not in simplified.keys():
            simplified[dict["name"]] = []
        for dict2 in list:
            if dict2["parent"] == dict["id"]:
                simplified[dict["name"]] += dict2["name"]
    return simplified

def index(request):
    #get request data and display
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All").json()["data"] #list of dictionaries
    
    #simplified_t = simplify(territories)

    print(territories[0])
    #print(f"{territories.json()}, {type(territories.json())}")
    #print(sorted(territories, key=lambda d:d["id"]))

    return render(request, 'index.html', {})