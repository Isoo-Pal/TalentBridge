from django.shortcuts import render
from .forms import *

# Create your views here.
def registration(request):
    user_form = UserRegisterForm()
    profile_form = UserProfileForm()
    return render(request, "users/registration.html", {'profile_form' : profile_form, 'user_form': user_form})