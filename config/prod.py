# config/prod.py

from .default import *

SECRET_KEY = '5e04a4955d8878191923e86fe6a0dfb24edb226c87d6c7787f35ba4698afc86e95cae409aebd47f7'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgres://zxkwnteczlnpro:09f47e077fcea7f793416dab6929549cb949585da92a78f90b643ad5ff60ef07@ec2-50-19-26-235.compute-1.amazonaws.com:5432/d4qm3c1bb9m6vj'