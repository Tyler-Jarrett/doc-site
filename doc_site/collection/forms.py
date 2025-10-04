from django import forms
from . import models

class EntrySubmission(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    password = forms.CharField(label='password', max_length=50)

class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }