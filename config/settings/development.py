from .base import *
from datetime import timedelta

AUTH_USER_MODEL = 'user.User'
DEBUG=True
ALLOWED_HOSTS=["*"]
DATABASES={
    'default' : {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'backend_starter_db',
        'USER' : 'postgres' ,
        'PASSWORD' : '784512369',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}