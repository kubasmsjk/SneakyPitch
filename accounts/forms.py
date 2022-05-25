from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from GamePLAY.models import *


# rejestracja
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    )
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Password again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password again'}),
    )

    class Meta:
        model = User

        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2'
        ]


# tworzenie druzyny
class DateInput(forms.DateInput):
    input_type = 'date'


class CreateTeam(ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'stadium_name', 'coach_name', 'creation_date', 'league_name')

        labels = {
            'team_name': 'Team name',
            'stadium_name': 'Stadium',
            'coach_name': 'Coach',
            'creation_date': 'Date',
            'league_name': 'League',

        }

        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'input-element', 'placeholder': 'Team name'}),
            'stadium_name': forms.TextInput(attrs={'class': 'input-element', 'placeholder': 'Stadium'}),
            'coach_name': forms.TextInput(attrs={'class': 'input-element', 'placeholder': 'Coach'}),
            'creation_date': DateInput(format='%d/%m/%Y', attrs={'class': 'input-date-element'})
        }


# tworzenie graczy
class CreatePlayers(ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'player_position', 'country','team')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'input-element1', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'input-element1', 'placeholder': 'Last name'}),
        }

# def clean(self, *args, **kwargs):
#     data = super().clean(*args, **kwargs)
#    if data['price'] < data['product'].price:
#      raise ValidationError('The price of the sale is below the price of the product')
#   return data
