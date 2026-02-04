from django.shortcuts import render
from .forms import *

# Create your views here.
def registration(request):
    form = UserForm()
    return render(request, "users/registration.html", {'form' : form})