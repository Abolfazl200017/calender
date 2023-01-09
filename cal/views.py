from webbrowser import get
from django.shortcuts import render
from . import utils
from datetime import datetime, date
import jdatetime

# Create your views here.
def callist(request, user_name):
    context = utils.get_cal()
    context['user_name']= user_name
    return render(request, 'cal.html', context=context)

def showday(request, user_name, date):
    darr = date.split('-')
    # d = datetime.date(year=int(darr[0]), month=int(darr[1]), day=int(darr[2]))
    d= jdatetime.date.fromgregorian(day=int(darr[2]), month=int(darr[1]), year=int(darr[0]))
    hours = utils.get_hours()
    return render(request, 'day_cal.html', {'date': d, 'hours': hours}) 