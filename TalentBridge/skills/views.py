from django.shortcuts import render, redirect
from .forms import addSkills
from .models import Skills
from django.contrib import messages


def AddSkills(request):
    if request.method == 'POST':
        skills_form = addSkills(request.POST)
        if skills_form.is_valid():
            skills = skills_form.save(commit=False)
            skills.user = request.user
            skills.save()
            messages.success(request, "Registration successful!!!")
            return redirect('users:dashboard')
        
    else:
        form = addSkills()
    return render(request, "skills/add-skills.html", {'form':form})