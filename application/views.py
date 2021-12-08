from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User, AnonymousUser
import requests
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/")

        
    return render(request, "application/index.html")

def images(request):
    return render(request, "application/images.html")

def dataleaks(request):
    
    context={}
    if request.method=="POST":
        try:
            domain=request.POST['domain']
            r=requests.get(f"http://127.0.0.1:8000/dataleaks/{domain}")
            data=r.json[f"{domain}"]

            context= {
                'dataleaks': data
            }
        except Exception as e:

            context= {
                'dataleaks': "Not Found"
            }

    return render(request, "application/dataleaks.html", context)

def domains(request):
    
    context={}
    if request.method=="POST":
        try:
            domain=request.POST['subdomain']
            r=requests.get(f"http://127.0.0.1:8000/subdomain/{domain}")
            data=r.json()[f"{domain}"]

            context= {
                'subdomain': data
            }
        except Exception as e:

            context= {
                'subdomain': "NOT FOUND"
            }

    return render(request, "application/domains.html", context)

def sensors(request):
    return render(request, "application/sensors.html")

def torrents(request):
    return render(request, "application/torrents.html")
