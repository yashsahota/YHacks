from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Office_Hour, User

from datetime import datetime as dt
import datetime



def course(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    live_list = Office_Hour.objects.filter(is_live=True)
    class_list = User.objects.filter(name="Ryan Slama")[0].course_enrolled.all

    presortold_list = Office_Hour.objects.filter(is_live=False).filter(end_time__lt=dt.now()).filter(is_completed=True) 
    old_list = []
    populated = False

    for x in range(0,7):
        end_time_calc = dt.now() - datetime.timedelta(days=x) - datetime.timedelta(minutes = 1)
        start_time_calc = end_time_calc - datetime.timedelta(days=1)
        old_list.insert(x, list(presortold_list.filter(start_time__lt=(end_time_calc), start_time__gt=(start_time_calc))))
        if(old_list[x] != []):
            populated = True

    if(populated == False):
        old_list = []


    preupcoming_list = Office_Hour.objects.filter(is_live=False).filter(start_time__gt=dt.now())

    upcoming_list = []

    populated = False

    for x in range(0,7):
        start_time_calc = dt.now() + datetime.timedelta(days=x) + datetime.timedelta(minutes = 1)
        end_time_calc = start_time_calc + datetime.timedelta(days=1)
        print("Range is ", start_time_calc, end_time_calc)
        upcoming_list.insert(x, list(preupcoming_list.filter(start_time__gt=(start_time_calc), start_time__lt=(end_time_calc))))
        if(upcoming_list[x] != []):
            populated = True

    if(populated == False):
        upcoming_list = []

    print("Live list is ", live_list)
    print("Class list is ", class_list)
    print("Upcoming list is", upcoming_list)
    print("Old list is ", old_list)
    context = {
        'live_list': live_list,
        'class_list': class_list,
        'old_list': old_list,
        'upcoming_list': upcoming_list,
    }
    template = loader.get_template('ruminate/app.html')
    return HttpResponse(template.render(context, request))
