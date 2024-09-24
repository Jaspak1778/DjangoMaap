# forms.py

from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description']

#haku
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)