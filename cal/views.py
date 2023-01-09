from webbrowser import get
from django.shortcuts import render
from . import utils
from datetime import datetime, date
import jdatetime
from django.contrib.auth.models import User
from todo.models import Todo

# Create your views here.
def callist(request, user_name):
    context = utils.get_cal()
    context['user_name']= user_name
    return render(request, 'cal.html', context=context)

def get_jdate(date):
    darr = date.split('-')
    return jdatetime.date.fromgregorian(day=int(darr[2]), month=int(darr[1]), year=int(darr[0]))

def get_todo(userid, date, i):
    todo = Todo.objects.filter(user=userid, date=date, time=i+1).first()
    if todo is None:
        todo = {
            'title': 'برنامه‌ای ثبت نشده است.',
            'islink': False,
        }
    else:
        if todo.private:
            todo = {
                'title': 'برنامه شخصی.',
                'islink': False,
            }
        else:
            todo = {
                'title': todo.title,
                'islink': True,
            }
    return todo

def get_day_todos(user_name, date):
    userid = User.objects.get(username=user_name).id
    todos=[]

    for i in range(12):
        todo = []
        tmp={
            'hour': i+1,
            'todo': get_todo(userid, date, i),
        }
        todo.append(tmp)
        tmp={
            'hour': i+13,
            'todo': get_todo(userid, date, i+12),
        }
        todo.append(tmp)
        todos.append(todo)
    return todos

def showday(request, user_name, date):
    d= get_jdate(date)
    hours = utils.get_hours()
    todos = get_day_todos(user_name, date)
    return render(request, 'day_cal.html', {'date': d, 'hours': hours, 'todos': todos}) 