from django.shortcuts import render, redirect
from django.urls import reverse
import requests

# Create your views here.

def login(request):
    c = {"message":""}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        payload = {'username':username, 'password':password}
        headers = {"Content-Type":"application/json", "accept": "text/plain"}
        response = requests.post("https://netzwelt-devtest.azurewebsites.net/Account/SignIn", json = payload, headers=headers)
        
        #print(response.json(), type(response.json()))
        signinResponse = response.json()
        
        if(response.ok == True):
            if((response.json()["username"] != None)): 
                #pass user data through redirect using session storage
                request.session["username"] = response.json()["username"]

                return redirect(reverse("home:index")) #required for redirects to other apps
        else:
            c["message"] = signinResponse["message"]
            return render(request, 'login.html', context=c)
    
    return render(request, 'login.html', context=c)
    