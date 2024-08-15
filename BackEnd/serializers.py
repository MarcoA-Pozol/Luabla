from rest_framework.serializers import Serializer, ModelSerializer
from Session.models import User
from App_Cards.models import Deck, Card

# User model serializers
class UserSerializer(ModelSerializer):
    """
        Serializer for general API methods (mostly)
    """
    class Meta:
        model = User
        fields = "__all__"

class ListUsersSerializer(ModelSerializer):
    """
        Customized serializer for list users.
    """
    class Meta:
        model = User
        # Do not admit the "password" field because it is a personal data.
        fields = ['id', 'username', 'country', 'email', 'gender', 'learning_goals', 'profile_picture']
        
class CreateUserSerializer(ModelSerializer):
    """
        Serializer to create new user.
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        
        
# App Cards Serializers
class CreateDeckSerializer(ModelSerializer):
    """
        Serializer to create new deck.
    """
    class Meta:
        model = Deck
        fields = ['title',  'author', 'description', 'is_shareable']
        
class CreateCardSerializer(ModelSerializer):
    """
        Serializer to create new card.
    """
    class Meta:
        model = Card
        fields = ['title', 'author', 'content', 'group']