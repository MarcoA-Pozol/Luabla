from django.db import models
from Session.models import User

class UserVocabulary(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    example = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vocabulary_words")
    
    def __str__(self):
        return self.word
    