from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='' , max_length=120, required=False,
                           widget= forms.TextInput
)
