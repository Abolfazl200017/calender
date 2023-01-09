from django.shortcuts import redirect, render
from .forms import CreateTodoForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def show_todo(request, user_name, date, order):
    userid = User.objects.get(username=user_name).id
    todo = Todo.objects.filter(user=userid, date=date, time=order)
    context = {
        'title': todo[0].title,
        'body': todo[0].body,
    }
    return render(request, 'todo.html', context=context)

def add_todo(request, user_name, date, order):
    if request.user.is_authenticated:
        if request.user.username == user_name:   
            if request.method == "POST":
                f = CreateTodoForm(request.POST)
                if f.is_valid():
                    cd = f.cleaned_data
                    Todo.objects.create(user=request.user, title=cd['title'], body=cd['body'], date=date, time=order, private=cd['private'], exepts=cd['exepts'])
                    messages.success(request, 'برنامه شما با موفقیت افزوده شد.', '✅')
                    return redirect('date', user_name=user_name, date=date)
            else:
                f = CreateTodoForm()
            return render(request, 'add_todo.html', {'form': f})
    return redirect('date', user_name=user_name, date=date)

def edit_todo(request, user_name, date, order):
    return redirect('home')