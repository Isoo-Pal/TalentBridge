from django.urls import path
from . import views

app_name = "skills"

urlpatterns = [
    path('add-skills/', views.AddSkills, name = "add-skills"),
]
