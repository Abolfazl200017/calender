from django.shortcuts import redirect, render
from .forms import CreateTodoForm
# Create your views here.

def show_todo(request, user_name, date, order):
    return redirect('home')

def add_todo(request, user_name, date, order):
    if request.method == "POST":
        pass
    else:
        f = CreateTodoForm()
    return render(request, 'todo.html', {'form': f})

def edit_todo(request, user_name, date, order):
    return redirect('home')