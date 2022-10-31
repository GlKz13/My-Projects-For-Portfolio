from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(required=False, widget=forms.TextInput(attrs={'id': 'searchForm', 'placeholder': 'Search what you need',
																		   'name': 'q'}))



