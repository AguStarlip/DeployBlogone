# config/staging.py

from .default import *


APP_ENV = APP_ENV_STAGING

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:425367309@localhost:5432/miniblog'