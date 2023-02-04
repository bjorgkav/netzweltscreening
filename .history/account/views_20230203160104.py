from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
import json

# Create your views here.

def login(request):
    #if logged in, redirect to home
    #if not, redirect to login

    #template = loader.get_template('login.html') #will automatically look for 'templates' folder
    #return HttpResponse(template.render())
    c = {"message":0}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        payload = {'username':username, 'password':password}
        response = requests.post("https://netzwelt-devtest.azurewebsites.net/Account/SignIn", json = payload)
        
        print(response.json(), type(response.json()))
        signinResponse = response.json()

        if(response.ok == True):
            print("SUCCESS!")
            
            return render(request, 'login.html', context=signinResponse)
        else:
            c["message"] = response.json()
    
    return render(request, 'login.html', context=c)
    