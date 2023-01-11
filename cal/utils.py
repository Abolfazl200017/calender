import calendar
import datetime
from datetime import date
from webbrowser import get
import jdatetime

def get_month_range(date):
    nextdate = date + jdatetime.timedelta(days=29)
    if nextdate.month != date.month:
        return 29
    else:
        nextdate = nextdate + jdatetime.timedelta(days=1)
        if nextdate.month != date.month:
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

def get_cal_2():
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

def get_cal(month_delta):
    today = jdatetime.date.today()
    md = int(month_delta)
    firstday = get_first_day(month_delta)
    monthrange = get_month_range(firstday)
    days=[]
    for i in range(monthrange):
        day=dict()
        day['date']= firstday+jdatetime.timedelta(days=i)
        day['is_prev']= today>day['date']
        day['is_today']= today==day['date']
        days.append(day)
    wd=[]
    for i in range(firstday.weekday()):
        wd.append(0)
    context = {
        'days': days,
        'today':today,
        'monthrange': monthrange,
        'startday': wd,
        'month': get_month_name(firstday.month),
        'year': firstday.year,
    }
    return context    
    
def get_first_day(month_delta):
    fd = jdatetime.date.today()
    month_delta = int(month_delta)
    if month_delta>0:
        for i in range(month_delta):
            mr = get_month_range(fd)
            fd += jdatetime.timedelta(days=mr)
    if month_delta<0:
        for i in range(abs(month_delta)):
            mr = get_month_range(fd)
            fd -= jdatetime.timedelta(days=mr)
    fd = jdatetime.date(fd.year,fd.month, 1)
    return fd

def jdate_to_string(date):
    return date.isoformat()