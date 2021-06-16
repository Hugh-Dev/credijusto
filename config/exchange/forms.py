from django import forms
from .models import *
from django.forms import TextInput, ModelForm

class TokenForm(forms.Form):
    token = forms.CharField(widget=TextInput(attrs={
	'class':'form-control form-control-sm',
	'label': 'token',
	'placeholder': 'Enter token',
	'title': 'Enter the token that has been assigned to you',
	'data-toggle': 'tooltip',
	'data-placement': 'top',
	}), required = True)

    class Meta:
        fields = '__all__'
        model = TokenModel