from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
import requests
import json

def index(request, context):
    #get request data and display
    return render(request, 'index.html', context)