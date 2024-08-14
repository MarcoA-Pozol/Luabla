from django import forms
from .models import Card, Deck

class CardForm(forms.ModelForm):
    card_image = forms.ImageField(required=False)
    
    class Meta:
        model = Card
        fields = {'title', 'content', 'group', 'card_image'}
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop the user from kwargs before calling super
        super().__init__(*args, **kwargs)
        if user:
            self.fields['group'].queryset = Deck.objects.filter(author=user)
        
    def save(self, author, commit=True):
        card = super().save(commit=False)
        card.title = self.cleaned_data['title']
        card.content = self.cleaned_data['content']
        card.group = self.cleaned_data['group']
        card.card_image = self.cleaned_data['card_image']
        card.author = author
        
        if commit:
            card.save(author)
        return card
        
class DeckForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea)
    is_shareable = forms.BooleanField()
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Deck
        fields = {'title', 'description', 'is_shareable', 'image'}
        
    def save(self, author, commit=True):
        deck = super().save(commit=False)
        deck.title = self.cleaned_data['title']
        deck.description = self.cleaned_data['description']
        deck.is_shareable = self.cleaned_data['is_shareable']
        deck.image = self.cleaned_data['image']
        deck.author = author
        
        if commit:
            deck.save(author)
        return deck

# #To validate formulary data during object creation.    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     data = cleaned_data.get('data')
        
    #     if data == "x" or data != "x" or data is not None or not data:
    #         self.add_error('data_field', 'error')   

    #     return cleaned_data