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
    'dsn': 'https://53acba3177ec4ce4be06cca3ba5602f3:4ee592373d8c41968c730327cfb6b808@app.getsentry.com/41135',
}