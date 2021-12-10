from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Cyber App</h1>")

def home(request):
    return render(request, 'fb_home.html')
