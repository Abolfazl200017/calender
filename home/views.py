from email import message
from django.shortcuts import render, redirect

from home.forms import SearchForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SearchForm

# Create your views here.

def search_bar(request):
    if request.method == "POST":
        cd = request.POST['searched']
        user = User.objects.filter(username=cd).first()
        if user is not None:
            return redirect('cal', cd)
        else:
            messages.error(request, 'کاربری با نام وارد شده وجود ندارد.', '❌')
            return redirect('home')
    else:
        return redirect('home')

def go_home(request):
    if request.user.is_authenticated:
        return redirect('cal', str(request.user.username))
    else:
        return redirect('login')
