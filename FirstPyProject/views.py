from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


def home(request):
    params = {}
    return render(request, "home.html", params)


def Form(request):
    params = {}
    return render(request,"form.html",params)


def contact(request):
    params = {}
    return render(request,"contact.html",params)
    

def showname(request):

    print(request.GET.get("UserName"))
    
    params = {
        "UserName" : request.GET.get("UserName"),
            "Phone_number" : request.GET.get("Phone_number"),
    "email" : request.GET.get("email"),
    "date" : request.GET.get("date"),
    "Full_Name" : request.GET.get("Full_Name"),
    "youtube" : request.GET.get("youtube"),
    "password" : request.GET.get("password"),
        }
    return render(request,"showDatafromForm.html",params)
