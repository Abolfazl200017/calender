from re import T
from webbrowser import get
from django.shortcuts import redirect, render
from .forms import CreateTodoForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User
import jdatetime

# Create your views here.
def get_jdate(date):
    darr = date.split('-')
    jdate= jdatetime.date.fromgregorian(day=int(darr[2]), month=int(darr[1]), year=int(darr[0]))
    # days=['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه']
    # day= days[jdatetime.weekday(jdate)]
    # months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    # month= months[jdate]
    # return {'weekday': day, 'day': jdate.day, 'month': month, 'year': jdate.year}
    return jdate

def show_todo(request, user_name, date, order):
    userid = User.objects.get(username=user_name).id
    todo = Todo.objects.filter(user=userid, date=date, time=order).first()
    if todo is not None:
        context = {
            'title': todo.title,
            'body': todo.body,
            'date': get_jdate(date),
            'isowner': request.user.username==user_name,
        }
        return render(request, 'todo.html', context=context)
    else:
        return redirect('date', user_name=user_name, date=date)

def add_todo(request, user_name, date, order):
    if request.user.is_authenticated:
        userid = User.objects.get(username=user_name).id
        if request.user.id == userid:
            todos =  Todo.objects.filter(user=userid, date=date, time=order).first()
            if todos is not None:
                return redirect('edit_todo', user_name=user_name, date=date, order=order)
            else:
                if request.method == "POST":
                    f = CreateTodoForm(request.POST)
                    if f.is_valid():
                        cd = f.cleaned_data
                        Todo.objects.create(user=request.user, title=cd['title'], body=cd['body'], date=date, time=order, private=cd['private'], exepts=cd['exepts'])
                        messages.success(request, 'برنامه شما با موفقیت افزوده شد.', '✅')
                        return redirect('date', user_name=user_name, date=date)
                else:
                    f = CreateTodoForm()
                return render(request, 'add_todo.html', {'form': f, 'isedit': False})
    return redirect('date', user_name=user_name, date=date)

def edit_todo(request, user_name, date, order):
    if request.user.is_authenticated:
        userid = User.objects.get(username=user_name).id
        if request.user.id == userid:
            todo =  Todo.objects.filter(user=userid, date=date, time=order).first()
            if request.method == "POST":
                f = CreateTodoForm(request.POST, instance=todo)
                if f.is_valid():
                    f.save()
                    messages.success(request, 'ویرایش با موفقیت انجام شد.', '✅')
                    return redirect('date', user_name=user_name, date=date)
            else:
                f = CreateTodoForm(instance=todo)
            return render(request, 'add_todo.html', {'form': f, 'isedit':True})
    return redirect('date', user_name=user_name, date=date)