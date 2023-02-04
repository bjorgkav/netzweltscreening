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

    def getID(self):
        return self.node_id
    
    def getName(self):
        return self.name

def setNodes(LIST):
    node_list = []
    for D in LIST:
        print(node(D["id"], D["name"], D["parent"]))
        node_list.append(node(D["id"], D["name"], D["parent"]))
    
    setChildren(node_list=node_list)

    for n in node_list:
        print(n)

    return node_list

def setChildren(node_list):
    for node in node_list:
        print("Current node is", node.getName(), node.getID())
        for node2 in node_list:
            if node2.getParent() == node.getID():
                #print(f"{node2.getName()} and {node.getName()}")
                node.getChildren().append(node2.getName())
                print(node.getChildren())
    
def removeLeaves(node_list):
    new_node_list = []
    for node in node_list:
        if node.getChildren() != []:
            new_node_list.append(node)
    return new_node_list


def index(request):
    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries

    print(territories)
    
    simplified_t = setNodes(territories)

    return render(request, 'index.html', {'t_dict': simplified_t})

    