from django.shortcuts import render
from .forms import CreateTodoForm
# Create your views here.

def todo(request, user_name, date, order):
    if request.method == "POST":
        pass
    else:
        f = CreateTodoForm()
    return 

def add_todo(request, user_name, date, order):
    return

def edit_todo(request, user_name, date, order):
    return