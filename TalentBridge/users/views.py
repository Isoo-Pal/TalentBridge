from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.


def registration(request):
    # if request.method == 'POST':
    #     print(request.POST)
    #     user_form = UserRegisterForm(request.POST)
    #     profile_form = UserProfileForm(request.POST)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()

    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         profile.save()
    #         messages.success(request, "Registration successful!!!")
    #         return redirect('login')
    #     else:
    #         messages.error(request, "Form Invalid!!!")
    # else:
    #     user_form = UserRegisterForm()
    #     profile_form = UserProfileForm()
    # messages.warning(request, "Registration successful!!!")
    # print(user_form.errors, profile_form.errors)
        
    # return render(request, "users/registration.html", {'profile_form' : profile_form, 'user_form': user_form})
    return redirect("users:login")