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
    return jdate

def show_todo(request, user_name, date, order):
    userid = User.objects.get(username=user_name).id
    todo = Todo.objects.filter(user=userid, date=date, time=order).first()
    if todo is not None:
        # if  todo.private or todo.exepts.filter(request.user.id) is not None or request.user.id==userid: 
        if (request.user in todo.exepts.all()) or not todo.private or request.user.id==userid:
            context = {
                'title': todo.title,
                'body': todo.body,
                'date': date,
                'isowner': request.user.username==user_name,
                'isprivate': todo.private,
                'hour': order,
                'exepts':todo.exepts.values
            }
            return render(request, 'todo.html', context=context)
        else:
            return redirect('date', user_name=user_name, date=date)
    else:
        if userid == request.user.id:
            return redirect('add_todo', user_name=user_name, date=date, order=order)
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
                        Todo.objects.create(user=request.user, title=cd['title'], body=cd['body'], date=date, time=order, private=cd['private'])
                        Todo.objects.filter(user=request.user, date=date, time=order).first().exepts.set(cd['exepts'])
                        messages.success(request, '???????????? ?????? ???? ???????????? ???????????? ????.', '???')
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
                    todo.exepts.set(f.cleaned_data['exepts'])
                    messages.success(request, '???????????? ???? ???????????? ?????????? ????.', '???')
                    return redirect('date', user_name=user_name, date=date)
            else:
                f = CreateTodoForm(instance=todo)
            return render(request, 'add_todo.html', {'form': f, 'isedit':True})
    return redirect('date', user_name=user_name, date=date)