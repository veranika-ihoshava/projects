from django import forms
from shop.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['applied_date']
    username = forms.CharField(label = 'Your name:', required=False)
    surname = forms.CharField(label = 'Your surname:', required=False)
    login = forms.EmailField(label = 'E-mail:')
    checked = forms.BooleanField(required=True)
