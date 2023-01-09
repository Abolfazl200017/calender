from dataclasses import fields
from django import forms
from .models import Todo

class CreateTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body', 'private', 'exepts']
