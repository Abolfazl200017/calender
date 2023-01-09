from django.shortcuts import render, redirect

# Create your views here.
def go_home(request):
    if request.user.is_authenticated:
        return redirect('cal', str(request.user.username))
    else:
        return redirect('login')
    return render(request, 'home.html')