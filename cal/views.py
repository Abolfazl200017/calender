from django.shortcuts import render
from . import utils
from datetime import datetime

# Create your views here.
def callist(request):
    return render(request, 'cal.html', {'days': utils.get_days(), 'start_day': utils.get_start_day()})