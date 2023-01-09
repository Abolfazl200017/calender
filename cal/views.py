from webbrowser import get
from django.shortcuts import render
from . import utils

# Create your views here.
def callist(request, user_name):
    context = utils.get_cal()
    return render(request, 'cal.html', context=context)

def showday(request, date):
    return render(request, 'day_cal.html', {'date': date})