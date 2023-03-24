from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    """
    A class to create registration form
    """
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in ['username', 'email', 'password1', 'password2']:
            self.fields[field].help_text = None


class LoginForm(AuthenticationForm):
    """
    A class to create LogIn form
    """
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'data-toggle': 'password',
            'id': 'password',
            'name': 'password',
            })
    )
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
