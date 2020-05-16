from django import forms
from django.contrib.auth.models import User
from django.core import validators
from .models import Donate, OrganizationName

CATEGORIES= [
    (1,'Home'),
    (2,'School'),
    (3,'Work'),
    (4,'Self-improvement'),
    (5,'Other'),
    ]

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField()
 
class DateInput(forms.DateInput):
    input_type= 'date'

class DonateForm(forms.Form):
	Wish= forms.CharField(max_length=100, label='What is your message?:')
	OrgName= forms.ModelChoiceField(queryset=OrganizationName.objects.all(),label ='Organization Name:')
	#txt_date = forms.DateField(widget=DateInput)
	Amount=forms.IntegerField(initial=0, label='Amount ($):')


class DonateAgainForm(forms.Form):
	Ids=forms.CharField(widget=forms.HiddenInput())
	Wish=forms.CharField(max_length=100, label='Wish')
	Category=forms.ModelChoiceField(queryset=OrganizationName.objects.all(),widget=forms.TextInput(attrs={'readonly':'readonly'}))
	Amount=forms.IntegerField(initial=0)
	Date=forms.DateField(widget=DateInput)

