from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    confirm_password = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=120, null=False)
    learning_goals = models.TextField()
    gender = models.CharField(max_length=10, null=False)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=False, unique=False, default="profile_pictures/default_profile_picture.jpg")
    agree_to_terms = models.BooleanField(null=False, default=False)
    
    def __str__(self):
        return self.username
    