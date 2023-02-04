from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
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
        headers={"Content-Type":"application/json", "accept": "text/plain"}
        response = requests.post("https://netzwelt-devtest.azurewebsites.net/Account/SignIn", json = payload, headers=headers)
        
        print(response.json(), type(response.json()))
        signinResponse = response.json()

        if((response.json()["username"] != None) and (response.ok == True)): 
            print("SUCCESS!")

            #pass user data through redirect using session storage
            request.session["username"] = response.json()["username"]
            request.session["displayName"] = response.json()["displayName"]
            request.session["roles"] = response.json()["roles"]

            return redirect("account:index") #required for redirects to other apps
        else:
            c["message"] = signinResponse["message"]
            return render(request, 'login.html', context=c)
    
    return render(request, 'login.html', context=c)
    