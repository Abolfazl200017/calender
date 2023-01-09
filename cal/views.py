from webbrowser import get
from django.shortcuts import render
from . import utils

# Create your views here.
def callist(request):
    context = utils.get_cal()
    return render(request, 'cal.html', context=context)

def showday(request, day_num):

    return render(request, 'day_cal.html', {'day_num': day_num})