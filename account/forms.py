from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100, label='Username or email')
    password = forms.CharField(max_length = 100, label='Password', widget = forms.PasswordInput)