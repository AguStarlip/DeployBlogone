# config/testing.py

from .default import *

# Parametros para activar el modo debug
TESTING = True
DEBUG = True

APP_ENV = APP_ENV_TESTING

WTF_CSRF_ENABLE = False