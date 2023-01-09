from dataclasses import fields
from email.quoprimime import body_check
from typing import Required
from django import forms
from setuptools import Require
from .models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body', 'private', 'exepts']
