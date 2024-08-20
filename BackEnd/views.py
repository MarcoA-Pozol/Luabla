from django.shortcuts import render
# Packages for customized APIs
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
# Generic API views
from rest_framework import generics
# Serializers
from . serializers import ListUsersSerializer, CreateUserSerializer, UserSerializer, CreateDeckSerializer, CreateCardSerializer
from Session.models import User
from App_Cards.models import Deck, Card

"""API VIews"""

# User API Views
class ListUsersView(APIView):
    """
        API View that can retrieve list of all users but only available to superusers and when they are authenticated using JWT.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        """
            Retrieve list of users without returning "password" for security as a second filter, the first is the JWT authorization required.
        """
        users = User.objects.all().values('id', 'username', 'country', 'email', 'gender', 'learning_goals', 'profile_picture')
        return Response(users, status = status.HTTP_200_OK)
    
class CreateUserView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class UpdateUserView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class DeleteUserView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
# Deck API Views
class ListDecksView(APIView):
    """
        API View that can retrieve a list of all decks from App_Cards Deck model.
    """
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        """
            Retrieve list of decks
        """
        decks = Deck.objects.all().values('id', 'title', 'author', 'description')
        return Response(decks, status = status.HTTP_200_OK)

class CreateDeckView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    
    serializer_class = CreateDeckSerializer
    queryset = Deck.objects.all()


# Card API Views
class ListCardsView(APIView):
    """
        API View that can retrieve a list of all cards from App_Cards Card model.
    """
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        """
            Retrieve a list of cards
        """
        cards = Card.objects.all().values('id', 'title', 'content', 'author', 'group')
        return Response(cards, status = status.HTTP_200_OK)
        
class CreateCardView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    
    serializer_class = CreateCardSerializer
    queryset = Card.objects.all()