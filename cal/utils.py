import calendar
from datetime import datetime
from webbrowser import get

def get_solar_calender_day(num):
    if num<5:
        return num+2
    else:
        return num-5
# this function returns the first day of this month
def get_start_day():
    num = calendar.monthrange(year=datetime.now().year, month=datetime.now().month)[0]
    days=[]
    for i in range(get_solar_calender_day(num)):
        days.append(i)
    return days


def get_month_range():
    return calendar.monthrange(year=datetime.now().year, month=datetime.now().month)[1]

def get_days():
    days=[]
    today = datetime.now().day
    for i in range(today):
        day = {
            'num': i+1,
            'is_prev': True,
            'is_today': False,
        }
        days.append(day)
    days.append({'num': today+1,'is_prev':False,'is_today':True})
    for i in range(today+1, get_month_range()):
        day = {
            'num': i+1,
            'is_prev': False,
            'is_today': False,
        }
        days.append(day)

    return days
