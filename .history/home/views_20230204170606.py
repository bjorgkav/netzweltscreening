from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json
from django.template.defaulttags import register

class node:
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
    print("")

def index(request):
    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries

    print(territories)
    
    #simplified_t = simplify(territories)

    #print(simplified_t)

    return render(request, 'index.html', {'t_dict': simplified_t})

    