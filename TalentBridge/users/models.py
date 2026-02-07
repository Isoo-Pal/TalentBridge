from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    address = models.TextField(blank=False)
    country = CountryField(blank=False)
    # state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=False)
    zip = models.IntegerField(blank=False)
    userType = models.CharField(max_length=100, blank=False)
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
