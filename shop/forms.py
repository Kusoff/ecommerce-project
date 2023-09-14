from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com')

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'birthday', 'phone', 'address')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())