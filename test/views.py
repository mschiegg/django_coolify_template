from django.shortcuts import render
from django.conf import settings


def start(request):
    return render(request, 'test/start.html', {
        'DEBUG': settings.DEBUG
    })
