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

def get_jdate(date):
    darr = date.split('-')
    return jdatetime.date.fromgregorian(day=int(darr[2]), month=int(darr[1]), year=int(darr[0]))

def showday(request, user_name, date):
    d= get_jdate(date)
    hours = utils.get_hours()
    return render(request, 'day_cal.html', {'date': d, 'hours': hours}) 