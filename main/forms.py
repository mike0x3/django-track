from django import forms

class searchPost(forms.Form):
	code = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Inserisci il codice di spedizione','type':'text'}))