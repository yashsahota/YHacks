from django.http import HttpResponse
from django.shortcuts import render

import datetime


def course(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'ruminate/app.html')
