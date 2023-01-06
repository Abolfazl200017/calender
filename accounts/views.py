from email import message
from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup_user(request):
    if(request.method=='POST'):
        f = RegisterUserForm(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            User.objects.create_user(cd['username'], '', cd['password'])
            messages.success(request, 'ورود شما با موفقیت انجام شد.', '✅')
            return redirect('home')
    else:
        f = RegisterUserForm()
    return render(request, 'register.html', {'form': f})

def login_user(request):
    return render(request, 'register.html', {"form":'test', 'type':'signup'})
