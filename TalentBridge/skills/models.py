from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Skills(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=50, blank=False)
    category = models.CharField(max_length=50)
    description = models.TextField()
    experience_level = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    availability = models.CharField(max_length=50)
    preferred_mode = models.CharField(max_length=50)
    price_type = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username
