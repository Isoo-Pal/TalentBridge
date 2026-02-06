from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    country = CountryField()
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    userType = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
