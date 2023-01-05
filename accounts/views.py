from email import message
from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterUserForm
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if(request.method=='POST'):
        f = RegisterUserForm(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            User.objects.create_user(cd['username'], '', cd['password'])
            message('تبریک', {'title':'✅'})
            return redirect('home')
    else:
        f = RegisterUserForm()
    return render(request, 'register.html', {'form': f})

def signup_user(request):
    return render(request, 'register.html', {"form":'test', 'type':'signup'})
