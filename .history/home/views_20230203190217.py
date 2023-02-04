from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def simplify(list):
    simplified = {}

    for dict in list:
        current_name = dict["name"]
        if current_name not in simplified.keys():
            simplified[current_name] = []
        
        for dict2 in list:
            if(dict2["parent"] == current_name):
                simplified[current_name] += dict2["parent"]
    return simplified

def index(request):
    #get request data and display
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All").json()["data"] #list of dictionaries
    
    simplified_t = simplify(territories)

    print(simplified_t)

    return render(request, 'index.html', {})