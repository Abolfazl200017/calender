from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if(request.method=='POST'):
            f = RegisterUserForm(request.POST)
            if f.is_valid():
                cd = f.cleaned_data
                User.objects.create_user(cd['username'], '', cd['password'])
                authenticate(username=cd['username'], password=cd['password'])
                messages.success(request, 'ثبت نام شما با موفقیت انجام شد.', '✅')
                return redirect('home')
        else:
            f = RegisterUserForm()
        return render(request, 'register.html', {'form': f, 'type': 'ثبت نام'})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        f = RegisterUserForm(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'ورود شما باموفقیت انجام شد.', '✅')
                return redirect('home')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشباه میباشد.', '❌')
    else:
        f=RegisterUserForm()
    return render(request, 'register.html', {'form': f, 'type':'ورود'})

def logout_user(request):
    logout(request)
    messages.error(request, 'از حساب کاربری خود خارج شدید.', '⚠️')
    return redirect('home')
