from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    email = forms.CharField(label="Email",
                            required=True,
                            max_length=75,
                            widget=forms.TextInput(
                                attrs={"id": "login-email",
                                        "title": "",
                                        "value": "",
                                        "autocapitalize": "off"}))
    password = forms.CharField(label="Password",
                            required=False,
                            widget=forms.PasswordInput(
                                render_value=False,
                                attrs={"id": "login-pass",
                                        "title": "",
                                        "value": ""}))

    def clean(self):
        error_msg = "The email and/or password \
                    you specified does not exist"
        try:
            user = User.objects.filter(
                email=self.cleaned_data['email'])[0]
        except IndexError:
            raise forms.ValidationError(error_msg)
        else:
            username = user.username
            auth_user = authenticate(username=username,
                        password=self.cleaned_data['password'])
            if auth_user:
                self.user = auth_user
            else:
                raise forms.ValidationError(error_msg)
        return self.cleaned_data

    def login(self, request):
        if self.is_valid():
            login(request, self.user)
            return True
        return False


