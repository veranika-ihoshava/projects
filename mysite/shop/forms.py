from django import forms
from shop.models import Application
from django.forms import fields

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['applied_date']
    username = forms.CharField(label = 'Your name:')
    surname = forms.CharField(label = 'Your surname:')
    login = forms.EmailField(label = 'E-mail:')