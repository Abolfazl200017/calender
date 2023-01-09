from email.policy import default
from django import forms
from .models import Todo

class CreateTodoForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField()
    # date = forms.DateTimeField()
    # time = forms.CharField(max_length=2)
    private = forms.BooleanField(default=False)
    exepts = forms.CharField(1)