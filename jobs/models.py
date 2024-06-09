from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()

class freelancer(models.Model):
    owner = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True)
    Skills = models.CharField(max_length=255, blank=True)
    Reviews = models.TextField(blank=True)
    Phone_number = models.CharField(max_length=20, blank=True)
    Email = models.EmailField(blank=True)


    def _str_(self):
        return f"{self.id} | {self.name}"
    

class business(models.Model):
    owner = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True)
    Reviews = models.TextField(blank=True)
    Phone_number = models.CharField(max_length=20, blank=True)
    Email = models.EmailField(blank=True)

    def _str_(self):
        return f"{self.id} | {self.name}"