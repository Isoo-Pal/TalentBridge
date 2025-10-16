from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request, "myapp/index.html")

def aboutUs(request):
    return render(request, "myapp/aboutUs.html")

def HowItWorks(request):
    return render(request, "myapp/howItWorks.html")


def skillMarketPlace(request):
    return render(request, "myapp/skillMarketplace.html")