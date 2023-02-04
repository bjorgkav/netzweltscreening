from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json
from django.template.defaulttags import register

def simplify(L):
    simplified = {}

    for dict in L:        
        #node is a parent? initialize a list
        if dict["name"] not in simplified.keys() and dict["parent"] == None:
            simplified[dict["name"]] = []
        else:#node is a child


    final_simplified = {}

    for region, subs in simplified.items(): #for each region and subregions
        if simplified.get(region) != []:
            final_simplified[region] = subs
            
    return final_simplified



def index(request):
    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries
    
    simplified_t = simplify(territories)

    print(simplified_t)

    return render(request, 'index.html', {'t_dict': simplified_t})

    