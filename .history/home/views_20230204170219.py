from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json
from django.template.defaulttags import register

class NODE:
    parent = ""
    children = []
    def __init__(self, parent, children) -> None:
        self.parent = parent
        self.children = children
    
    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.pop(child)

    def setParent(self, parent):
        self.parent = parent

def simplify(L):
    simplified = {}

    for dict in L:
        
        #initialize a list
        if dict["name"] not in simplified.keys():
            simplified[dict["name"]] = []


        for dict2 in L:
            #node is a child of other node
            if(dict2["parent"] == dict["id"]): 
                simplified[dict["name"]].append(dict2["name"])

    print(simplified)

    final_simplified = {}

    for region, subs in simplified.items(): #for each region and subregions
        if simplified.get(region) != []:
            final_simplified[region] = subs

    print(f"\n\n {final_simplified}")

    for key in final_simplified.keys(): #for each region
        for terrlist in final_simplified.values(): #for each of the subregions
            if key in terrlist:
                terrlist[terrlist.index(key)] = {key:final_simplified.get(key)}
            

    print(f"\n\n {final_simplified}")
            
    return final_simplified

def index(request):
    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries
    
    simplified_t = simplify(territories)

    print(simplified_t)

    return render(request, 'index.html', {'t_dict': simplified_t})

    