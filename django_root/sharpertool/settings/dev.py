print("Loading development settings.")

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = "bungus"

RAVEN_CONFIG = {
    'dsn': 'https://53acba3177ec4ce4be06cca3ba5602f3:4ee592373d8c41968c730327cfb6b808@app.getsentry.com/41135',
}