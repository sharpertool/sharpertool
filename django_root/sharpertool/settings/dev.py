print("Loading development settings.")

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = "bungus"

RAVEN_CONFIG = {
    'dsn': 'https://959ab970310d45b18f07b40cfa365517:abf36a6715774ba182ca01dee91df778@app.getsentry.com/41135',
}