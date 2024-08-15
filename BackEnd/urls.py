from django.urls import path
from .views import ListUsersView, CreateUserView, CreateDeckView, CreateCardView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # User API Views
    path("user/list/", ListUsersView.as_view(), name="api-list-users"),
    path("user/create/", CreateUserView.as_view(), name="api-create-user"),
    # Deck(App_Cards) API Views
    path("deck/create/", CreateDeckView.as_view(), name="api-create-deck"),
    # Card(App_Cards) API Views
    path("card/create/", CreateCardView.as_view(), name="api-create-card"),
    # JWT management urls for the Token
    path("token/get/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]

