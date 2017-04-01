from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    currentDateTime = (datetime.datetime.strftime(now, '%b %-d, %Y %-I:%M %p'))

    context={
    "currentDateTime":currentDateTime
    }
    return render(request, 'timedisplay/index.html', context)
