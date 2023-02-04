from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.template.defaulttags import register

class node:
    node_id = 0
    name = ""
    parent = None

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

    return node_list

def setChildren(node_list):
    for node in node_list:
        for node2 in node_list[1:]:
            if node2.getParent() == node.getID():
                node.addChild(node2)

def showChildren(node_list):
    for n in node_list:
        print(f"Node {n.getName()} has {n.getChildCount()} children." if n.getChildCount() > 0 else f"Node {n.getName()} has no children.")

def index(request):

    if "username" not in request.session: #test if username argument even exists
        return redirect(reverse("account:login"))

    #get request data and display
    headers = {"accept": "*/*"}
    territories = requests.get("https://netzwelt-devtest.azurewebsites.net/Territories/All", headers=headers).json()["data"] #list of dictionaries
    
    simplified_t = setNodes(territories)

    return render(request, 'index.html', {'node_list': simplified_t})

def redirect_index(request):
    return redirect(reverse('home:index'))