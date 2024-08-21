from django.forms import ModelForm
from .models import *
from django import forms
from django.core.validators import EmailValidator


class ContactFormeng(forms.ModelForm):
    
    name = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Full Name','class':'form-control'}))
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email address','class':'form-control'}))
    phone = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Phone number','class':'form-control'}))
    message = forms.Textarea( )
   
    class Meta:
        model = contact
        fields = ['name', 'email', 'phone' , 'message']

class ContactFormfr(forms.ModelForm):
    name = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Nom complet','class':'form-control'}))
    email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email ','class':'form-control'}))
    phone = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Numero téléphone','class':'form-control'}))
    message = forms.Textarea( )
   
    class Meta:
        model = contact
        fields = ['name', 'email', 'phone' , 'message']