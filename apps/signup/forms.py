from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from account import utils


class SignupForm(forms.Form):

    email = forms.EmailField(
                widget=forms.TextInput(
                attrs={'id': "signup-email",
                        'title': "Email Address",
                        'class': "forminput"}))
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) > 75:
            raise forms.ValidationError(
                    'Email must be less than 75 characters')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise forms.ValidationError(
                    'This email is already signed up.')

    def get_user(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = utils.generate_user(email, password)
        auth_user = authenticate(username=user.username,
                                password=password)
        return auth_user
