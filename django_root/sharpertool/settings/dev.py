print("Loading development settings.")

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = "bungus"
