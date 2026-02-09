from django.shortcuts import render
from .forms import *

# Create your views here.
def registration(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            print("Form saved")
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, "users/registration.html", {'profile_form' : profile_form, 'user_form': user_form})