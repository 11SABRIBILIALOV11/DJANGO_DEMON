from django.db import models


class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


class Meta:
    app_label = 'DJANGO_DEMON'

