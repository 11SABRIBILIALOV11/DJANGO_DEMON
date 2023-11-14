# Файл: yourprojectname/urls.py
from django.urls import path
from DJANGO_DEMON.views import log_entry

urlpatterns = [
    path('log/', log_entry, name='log_entry'),
]

