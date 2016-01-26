# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import

print("Loading production settings.")

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sharpertool',
        'USER': 'sharper_user',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


RAVEN_CONFIG = {
    'dsn': 'https://959ab970310d45b18f07b40cfa365517:abf36a6715774ba182ca01dee91df778@app.getsentry.com/41136',
}