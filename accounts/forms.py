from django import forms

class RegisterUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()