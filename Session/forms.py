from django import forms
from .models import User

COUNTRIES= [
    ['Argentina', 'Argentina'],
    ['Brazil', 'Brazil'],
    ['China', 'China'],
    ['Colombia', 'Colombia'],
    ['Egypt', 'Egypt'],
    ['France', 'France'],
    ['Germany', 'Germany'],
    ['India', 'India'],
    ['Italy', 'Italy'],
    ['Japan', 'Japan'],
    ['Korea', 'Korea'],
    ['Mexico', "Mexico"],
    ['Russia', 'Russia'],
    ['Spain', 'Spain'],
    ['United States of America', 'United States of America'],
]

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=20)
    country = forms.ChoiceField(choices=COUNTRIES)
    gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    profile_picture = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'country', 'learning_goals', 'gender', 'profile_picture', 'agree_to_terms']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        agree_to_terms = cleaned_data.get('agree_to_terms')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        if not agree_to_terms:
            self.add_error('agree_to_terms', "You have to agree with terms and conditions to continue.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        user.country = self.cleaned_data['country']
        user.gender = self.cleaned_data['gender']
        user.profile_picture = self.cleaned_data['profile_picture']
        user.agree_to_terms = self.cleaned_data['agree_to_terms']
        
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    