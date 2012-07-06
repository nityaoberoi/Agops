from django import forms
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

    def get_user(self, request):
        email = self.cleaned_data['email']
        user = utils.generate_user(email)
        return user
