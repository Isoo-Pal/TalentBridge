from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', views.registration, name="registration"),
    path('login/', auth_views.LoginView.as_view(), name = "login"),
]
