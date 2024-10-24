from django.db import models
from Authentication.models import User

# class FriendRequest(models.Model):
#     from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     accepted = models.BooleanField(default=False)

#     def accept(self):
#         """Accept the friend request and add both users to each other's friend list."""
#         self.to_user.friends.add(self.from_user)
#         self.from_user.friends.add(self.to_user)
#         self.accepted = True
#         self.save()

#     def decline(self):
#         """Decline the friend request."""
#         self.delete()
        
class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friend_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sender', 'receiver')  # Prevent duplicate requests

    def __str__(self):
        return f"{self.sender} sent a friend request to {self.receiver}"

class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend1_set')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend2_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')  # Prevent duplicate friendships

    def __str__(self):
        return f"{self.user1} is friends with {self.user2}"