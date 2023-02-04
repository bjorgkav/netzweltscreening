from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json
from django.template.defaulttags import register

class node:
    node_id = 0
    name = ""
    parent = 0
    children = []
    def __init__(self, id, name, parent) -> None:
        self.node_id = id
        self.name = name
        self.parent = parent

    def __str__(self) -> str:
        return f"ID: {self.node_id}\nNode: {self.name}\nParent: {self.parent}\nChildren: {self.children}"
    
    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.pop(child)

    def setParent(self, parent):
        self.parent = parent

def setNodes(LIST):
    node_list = []
    for D in LIST:
        print(node(D["id"], D["name"], D["parent"]))
        node_list.append(node(D["id"], D["name"], D["parent"]))

    return node_list


def simplify(L):
    return 0

def index(request):
    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries

    print(territories)
    
    simplified_t = setNodes(territories)

    return render(request, 'index.html', {'t_dict': simplified_t})

    