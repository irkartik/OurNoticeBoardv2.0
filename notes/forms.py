from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
from notes.models import Note

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
