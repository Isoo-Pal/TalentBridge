from django.shortcuts import render
from .forms import *

# Create your views here.
def registration(request):
    if request.method == 'POST':
        print(request.POST)
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        print(user_form.is_valid(), profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            print("Form saved")
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()

    print(user_form.errors, profile_form.errors)
        
    return render(request, "users/registration.html", {'profile_form' : profile_form, 'user_form': user_form})