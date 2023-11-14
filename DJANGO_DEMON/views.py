# Файл: yourappname/views.py
from django.http import HttpResponse
from .models import LogEntry


def log_entry(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            log = LogEntry(message=message)
            log.save()
            return HttpResponse('Log entry saved successfully!')
        else:
            return HttpResponse('Empty message!')
    else:
        return HttpResponse('Invalid request method!')
