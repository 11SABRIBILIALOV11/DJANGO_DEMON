
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Остальные настройки в файле settings.py

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['DJANGO_DEMON.com']
ROOT_URLCONF = 'DJANGO_DEMON.urls'

# Настройки логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'DJANGO_DEMON.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

# Остальные настройки в файле settings.py
INSTALLED_APPS = [
    'DJANGO_DEMON'
]