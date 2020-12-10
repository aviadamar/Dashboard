from decouple import config
import dj_database_url

DATABASE = config('DATABASE')
DATABASE_URL = config('DATABASE_URL')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = int(config('PORT'))
SECRET_KEY = config('SECRET_KEY').encode('utf-8')

DATABASES = {'default': dj_database_url.config()}
