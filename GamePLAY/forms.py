from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('address',)
        labels = {
            'address': ''

        }
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Type here'})
        }