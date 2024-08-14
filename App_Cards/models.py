from django.db import models
from Session.models import User

class PreInstalledDeck(models.Model):
    title = models.CharField(null=False, max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="luabla_deck_author", default=8)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class PreInstalledCard(models.Model):
    title = models.CharField(null=False, max_length=100)
    content = models.TextField()
    group = models.ForeignKey(PreInstalledDeck, on_delete=models.CASCADE, related_name="luabla_deck")
    last_review = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="luabla_card_author", default=8)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Deck(models.Model):
    title = models.CharField(null=False, default="Default Group", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deck_author")
    description = models.TextField()
    is_shareable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owners = models.ManyToManyField(User, related_name="owners")
    downloads = models.IntegerField(default=0)
    image = models.ImageField(upload_to="deck_images/", unique=False, default="deck_images/default_deck_image.jpg")
       
    def __str__(self):
        return self.title
    
class Card(models.Model):
    title = models.CharField(null=False, max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="card_author")
    group = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="deck")
    last_review = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    card_image = models.ImageField(upload_to="card_images/", unique=False, default="card_images/default_card_image.jpg")
    
    def __str__(self):
        return self.title
    
