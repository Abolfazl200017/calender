from webbrowser import get
from django.shortcuts import render, redirect
from . import utils
from datetime import datetime, date
import jdatetime
from django.contrib.auth.models import User
from todo.models import Todo

# Create your views here.
def callist(request, user_name, month_delta):
    user = User.objects.filter(username=user_name).first()
    if user is not None:
        context = utils.get_cal(month_delta)
        context['user_name']= user_name
        return render(request, 'cal.html', context=context)
    else:
        return redirect('home')    

def get_jdate(date):
    today = jdatetime.datetime.strptime(date, '%Y-%m-%d').date()
    jdate = {}
    days = ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنجشنبه', 'جمعه']
    jdate['weekday'] = days[today.weekday() -1] 
    months=['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    jdate['month']=months[today.month - 1]
    jdate['day']=today.day
    return jdate

def get_title(request, userid, date, i):
    todo = Todo.objects.filter(user=userid, date=date, time=i).first()
    if todo is None:
        title = 'برنامه‌ای ثبت نشده است'
    else:
        if todo.private and ((request.user.id==userid) or (request.user in todo.exepts.all())):
            title = todo.title
        else:
            title = 'برنامه شخصی'
    return title

def get_day_todos(request, user_name, date):
    userid = User.objects.get(username=user_name).id
    todos=[]

    for i in range(12):
        todo = []
        tmp={
            'hour': i+1,
            'title': get_title(request, userid, date, i+1),
        }
        todo.append(tmp)
        tmp={
            'hour': i+13,
            'title': get_title(request, userid, date, i+13),
        }
        todo.append(tmp)
        todos.append(todo)
    return todos

def showday(request, user_name, date):
    d= get_jdate(date)
    todos = get_day_todos(request, user_name, date)
    return render(request, 'day_cal.html', {'date': d, 'todos': todos}) 