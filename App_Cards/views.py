from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Card, Deck
from.forms import CardForm, DeckForm

"""Views"""
@login_required
def cards(request):
    return render(request, 'cards.html')

@login_required
def review_cards(request):
    #Get self user decks and added decks from another user.
    own_decks = Deck.objects.filter(author=request.user).all()
    decks = Deck.objects.filter(owners=request.user).all()
    
    context = {'decks':decks, 'own_decks': own_decks}
    return render(request, 'review_cards.html', context)

@login_required
def create_card(request):
    #Get authenticated user decks
    decks = Deck.objects.filter(author=request.user).all()
    
    if request.method == 'POST':
        card_form = CardForm(request.POST, user=request.user)
        deck_form = DeckForm(request.POST)
    else:
        card_form = CardForm(user=request.user)
        deck_form = DeckForm()
    
    context = {'card_form':card_form, 'deck_form':deck_form, 'decks':decks}
    return render(request, 'create_card.html', context)

@login_required
def discover_decks(request):
    #Get all cards groups from every author that are shareable
    user = request.user
    decks = Deck.objects.filter(is_shareable=True).all()
    
    context = {'decks':decks, 'user':user}
    return render(request, 'discover_cards_group.html', context)



"""Views Functions"""
@login_required
def get_deck(request, deck_identifier):
    if request.method == "POST":
        user = request.user
        deck = Deck.objects.get(id=deck_identifier)
        deck.owners.add(user)
        return redirect('review_cards')
    else:
        return redirect('cards')
    
# Add Card / Deck
@login_required
def ACTION_add_card(request):
    if request.method == "POST":
        card_form = CardForm(request.POST)
        if card_form.is_valid():
            #Create new Card
            card = card_form.save(commit=False, author=request.user)
            card.save()
            return redirect('create_card')
    else:
        card_form = CardForm()
    

@login_required
def ACTION_add_deck(request):
    if request.method == "POST":
        deck_form = DeckForm(request.POST)
        if deck_form.is_valid():
            #Create new Cards Group
            deck = deck_form.save(commit=False, author=request.user)
            deck.save()
            return redirect('discover_decks')
    else:
        deck_form = DeckForm()
    