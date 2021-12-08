from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def data(request):
    return render(request, "website/data.html")

def pricing(request):
    return render(request, "website/pricing.html")

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")

def blog(request):
    return render(request, "website/blog.html")

def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect("/application")
        else:
            return redirect("/") 
    return HttpResponse("404 NOT FOUND")


def signupuser(request):

    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        myuser=User.objects.create_user(username, email,  password1)
        myuser.fname=firstname
        myuser.lname=lastname
        myuser.save()
        messages.success(request, "Successfully created user")
        return redirect("/")
        
    return HttpResponse("404 not found")


def logoutuser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/")