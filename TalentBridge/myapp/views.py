from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request, "myapp/home.html")
