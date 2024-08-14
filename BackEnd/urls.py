from django.urls import path
from .views import ListUsersView, CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("user/list/", ListUsersView.as_view(), name="api-list-users"),
    path("user/create/", CreateUserView.as_view(), name="api-create-user"),
    # JWT management urls for the Token
    path("token/get/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]

