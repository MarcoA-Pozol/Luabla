from django.urls import path
from . import views

urlpatterns = [
    path('', views.cards, name="cards"),
    path('create/', views.create_card, name="create_card"),
    path('review/', views.review_cards, name="review_cards"),
    path('discover_decks/', views.discover_decks, name="discover_decks"),
    path('get_deck/<int:deck_identifier>/', views.get_deck, name="get_deck"),
    #ACTION URLs
    path('ACTION_add_card/', views.ACTION_add_card, name="ACTION_add_card"),
    path('ACTION_add_deck/', views.ACTION_add_deck, name="ACTION_add_deck"),
]
