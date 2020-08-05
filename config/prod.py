# config/prod.py

from .default import *

SECRET_KEY = '5e04a4955d8878191923e86fe6a0dfb24edb226c87d6c7787f35ba4698afc86e95cae409aebd47f7'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'postgres://kldegntimmzaie:e3da2dd0a20dbbf9be71472897ed14a45183f98a3473dbb4a1c123a162ab0c91@ec2-34-197-212-240.compute-1.amazonaws.com:5432/d3n7m9044lio17'