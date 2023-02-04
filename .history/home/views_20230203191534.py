from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def simplify(L):
    simplified = {}

    for dict in L:
        
        if dict["name"] not in simplified.keys():
            simplified[dict["name"]] = []
        
        for dict2 in L:
            if(dict2["parent"] == dict["id"]):
                simplified[dict["name"]].append(dict2["name"])

    return simplified

def index(request):
    #get request data and display
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All").json()["data"] #list of dictionaries
    
    simplified_t = simplify(territories)

    print(simplified_t)

    return render(request, 'index.html', {})