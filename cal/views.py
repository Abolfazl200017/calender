from webbrowser import get
from django.shortcuts import render
from . import utils

# Create your views here.
def callist(request):
    context = utils.get_cal()
    return render(request, 'cal.html', context=context)