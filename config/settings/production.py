from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend_prod_db',
        'USER': 'postgres',
        'PASSWORD': '784512369',
        'HOST': 'prod-db-host',
        'PORT': '5432',
    }
}
