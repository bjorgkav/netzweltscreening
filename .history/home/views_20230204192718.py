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
    isChild = False

    children = []
    def __init__(self, id, name, parent) -> None:
        self.node_id = id
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self) -> str:
        return f"\nID: {self.node_id}\nNode: {self.name}\nParent: {self.parent}\nChildren: {self.children}\n"

    def addChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.pop(child)

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent
    
    def getChildren(self):
        return self.children

    def getChildCount(self):
        return len(self.children)

    def getID(self):
        return self.node_id
    
    def getName(self):
        return self.name

def setNodes(LIST):
    node_list = []
    for D in LIST:
        node_list.append(node(D["id"], D["name"], D["parent"]))
    
    setChildren(node_list=node_list)

    #removeChildren(node_list=node_list)

    #for n in node_list:
    #    print(n)

    return node_list

def setChildren(node_list):
    for node in node_list:
        #print("Current node is", node.getName(), node.getID())
        for node2 in node_list[1:]:
            if node2.getParent() == node.getID():
                node.addChild(node2)
                #print(node.getChildren())

def showChildren(node_list):
    for n in node_list:
        print(f"Node {n.getName()} has {n.getChildCount()} children." if n.getChildCount() > 0 else f"Node {n.getName()} has no children.")

def removeChildren(node_list):
    for n in node_list:
        if n.getChildCount() == 0:
            node_list.pop(node_list.index(n))

def index(request):
    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries

    #print(territories)
    
    simplified_t = setNodes(territories)

    for n in simplified_t:
        print(n)

    return render(request, 'index.html', {'node_list': simplified_t})

    