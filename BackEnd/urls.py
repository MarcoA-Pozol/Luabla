from django.urls import path
from .views import ListUsersView, CreateUserView, UpdateUserView, DeleteUserView, ListDecksView, CreateDeckView, ListCardsView, CreateCardView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # User API Views
    path("user/list/", ListUsersView.as_view(), name="api-list-users"),
    path("user/create/", CreateUserView.as_view(), name="api-create-user"),
    path("user/update/<int:pk>", UpdateUserView.as_view(), name="api-update-user"),
    path("user/delete/<int:pk>", DeleteUserView.as_view(), name="api-delete-user"),
    # Deck(App_Cards) API Views
    path("deck/list/", ListDecksView.as_view(), name="api-list-decks"),
    path("deck/create/", CreateDeckView.as_view(), name="api-create-deck"),
    # Card(App_Cards) API Views
    path("card/list/", ListCardsView.as_view(), name="api-list-cards"),
    path("card/create/", CreateCardView.as_view(), name="api-create-card"),
    # JWT management urls for the Token
    path("token/get/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]

