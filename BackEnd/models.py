from django.db import models
from Luabla import settings

class Notification(models.Model):
    reason = models.CharField(max_length=150)
    message = models.TextField()
    destinatary = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message