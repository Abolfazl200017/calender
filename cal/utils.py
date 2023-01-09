import calendar
import datetime
from datetime import date
from webbrowser import get
import jdatetime

def get_month_range(date):
    nextdate = date - jdatetime.timedelta(days=-29)
    if nextdate.month == date.month +1:
        return 29
    else:
        nextdate = nextdate - jdatetime.timedelta(days=-1)
        if nextdate.month == date.month + 1:
            return 30
        else:
            return 31

def get_month_name(num):
    month=['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    return month[num-1]

def get_solar_calender_day(num):
    if num<5:
        return num+2
    else:
        return num-5

def get_calendar_req():
    today = jdatetime.date.today()
    first = date.today() - datetime.timedelta(days=today.day - 1)
    firstday = date.weekday(first)
    morange = get_month_range(today - jdatetime.timedelta(days=today.day - 1))
    return {'firstdate': first, 'month': get_month_name(today.month), 'morange': morange, 'firstday': get_solar_calender_day(firstday), 'today': today}

def get_cal():
    requirement = get_calendar_req()
    print(requirement)
    days=[]
    for i in range(requirement['today'].day -1):
        day = {
            'date': requirement['firstdate'] - datetime.timedelta(days=-i),
            'jdate': requirement['today'] - jdatetime.timedelta(days=-i),
            'num': i+1,
            'is_prev': True,
            'is_today': False,
        }
        days.append(day)
    days.append({
        'date': requirement['firstdate'] - datetime.timedelta(days=-(requirement['today'].day-1)),
        'jdate': requirement['today'] - jdatetime.timedelta(days=-(requirement['today'].day-1)),
        'num': requirement['today'].day,
        'is_prev': False,
        'is_today': True,
    })
    for i in range(requirement['today'].day, requirement['morange']):
        day = {
            'date': requirement['firstdate'] - datetime.timedelta(days=-i),
            'jdate': requirement['today'] - jdatetime.timedelta(days=-i),
            'num': i+1,
            'is_prev': False,
            'is_today': False,
        }
        days.append(day)
    startday=[]
    for i in range(requirement['firstday']):
        startday.append(0)
    context = {
        'days': days,
        'monthrange': requirement['morange'],
        'startday': startday,
        'month': requirement['month'],
        'year': requirement['today'].year,
    }
    return context