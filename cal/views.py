from webbrowser import get
from django.shortcuts import render, redirect
from . import utils
from datetime import datetime, date
import jdatetime
from django.contrib.auth.models import User
from todo.models import Todo

# Create your views here.
def callist(request, user_name):
    user = User.objects.filter(username=user_name).first()
    if user is not None:
        context = utils.get_cal()
        context['user_name']= user_name
        return render(request, 'cal.html', context=context)
    else:
        return redirect('home')    

def get_jdate(date):
    darr = date.split('-')
    return jdatetime.date.fromgregorian(day=int(darr[2]), month=int(darr[1]), year=int(darr[0]))

def get_title(userid, date, i):
    todo = Todo.objects.filter(user=userid, date=date, time=i).first()
    if todo is None:
        title = 'برنامه‌ای ثبت نشده است'
    else:
        if todo.private:
            title = 'برنامه شخصی'
        else:
            title = todo.title
    return title

def get_day_todos(user_name, date):
    userid = User.objects.get(username=user_name).id
    todos=[]

    for i in range(12):
        todo = []
        tmp={
            'hour': i+1,
            'title': get_title(userid, date, i+1),
        }
        todo.append(tmp)
        tmp={
            'hour': i+13,
            'title': get_title(userid, date, i+13),
        }
        todo.append(tmp)
        todos.append(todo)
    return todos

def showday(request, user_name, date):
    d= get_jdate(date)
    todos = get_day_todos(user_name, date)
    return render(request, 'day_cal.html', {'date': d, 'todos': todos}) 