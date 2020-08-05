# config/default.py

from os.path import abspath, dirname, join

# Define el directorio de la aplicacion
BASE_DIR = dirname(dirname(abspath(__file__)))

# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POST_IMAGE_DIR = join(MEDIA_DIR, 'posts')

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

# Configuracion de base de datos
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Entornos de la aplicacion
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''

# Configuracion del email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'lipchak09@gmail.com'
MAIL_PASSWORD = '425367309'
DONT_REPLY_FROM_EMAIL = '(Agus, lipchak09@gmail.com)'
ADMINS = ('admin@xyz.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False

ITEMS_PER_PAGE = 6