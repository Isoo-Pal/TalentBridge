from django.urls import path
from . import views

app_name = "skills"

urlpatterns = [
    path('dashboard/', views.Dashboard, name = "dashboard"),
]
