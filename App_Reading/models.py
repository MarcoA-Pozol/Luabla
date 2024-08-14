from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200, null=False)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    front_image = models.ImageField(upload_to="stories_front_images/", null=False, unique=True)
    english_level = models.CharField(max_length=5, choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')])
    
    def __str__(self):
        return self.title