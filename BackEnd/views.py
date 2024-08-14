from django.shortcuts import render
# Packages for customized APIs
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
# Generic API views
from rest_framework import generics
# Serializers
from . serializers import ListUsersSerializer, CreateUserSerializer, UserSerializer
from Session.models import User

# API Views
class ListUsersView(APIView):
    """
        API View that can retrieve list of all users but only available to superusers and when they are authenticated using JWT.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        """
            Retrieve list of users without returning "password" for security as a second filter, the first is the JWT authorization required.
        """
        users = User.objects.all().values('username', 'country', 'email', 'gender', 'learning_goals', 'profile_picture')
        return Response(users, status = status.HTTP_200_OK)
    
class CreateUserView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    serializer_class = UserSerializer
    queryset = User.objects.all()