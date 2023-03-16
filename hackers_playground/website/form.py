from datetime import date

from django.forms import ModelForm, DateInput, TextInput, EmailInput
from django.core.exceptions import ValidationError
from django import forms
from .models import User
import re

class RegisterForm(ModelForm):
    secret_key = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter secret key'}), required=True)
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm password'}), required=True)
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={"type": "text", "placeholder": "Enter Username"}),
            'password': TextInput(attrs={"type": "text", "placeholder": "Enter Password"}),
            'email_id': EmailInput(attrs={"type": "email", "placeholder": "Enter email"}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError('Name must only contain letters.')
        return name

    def clean_email_id(self):
        email_id = self.cleaned_data['email_id']
        if '@' not in email_id:
            raise ValidationError('Invalid email address.')
        return email_id
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.search("[a-z]", password):
            raise ValidationError("Password must contain at least 1 lowercase letter.")
        elif not re.search("[A-Z]", password):
            raise ValidationError("Password must contain at least 1 uppercase letter.")
        elif not re.search("[!@#$%^&*()_+-={}|\\:;\"<>,.?/~`]", password):
            raise ValidationError("Password must contain at least 1 special character.")
        return password
    
    def clean_secret_key(self):
        secret_key = self.cleaned_data['secret_key']
        # Check if the secret key is valid here
        if secret_key != 'valid_secret_key':
            raise forms.ValidationError('Invalid secret key')
        return secret_key
