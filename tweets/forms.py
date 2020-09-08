from django import forms
from .models import Tweet


class TweetForm(forms.Form):
    #fields['country'].widget = forms.HiddenInput()
    text = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 1, 'cols': 85}), max_length=160)
    country = forms.CharField(
        widget=forms.HiddenInput(attrs={'value': "Hungary"}))


class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for',
                            widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'}))


class SearchHashTagForm(forms.Form):
    query = forms.CharField(label='Enter keyword to search hashTag for',
                            widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control search-hash-tag-query typeahead'}))
