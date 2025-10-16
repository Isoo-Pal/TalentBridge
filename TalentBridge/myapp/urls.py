from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('about-us/', views.aboutUs, name = "about-us"),
    path('how-it-works/', views.HowItWorks, name = "how-it-works"),
    path('skill-marketplace/', views.skillMarketPlace, name = "skill-marketplace"),
]
