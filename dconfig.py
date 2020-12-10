from decouple import config

DATABASE = config('DATABASE')
DATABASE_URL = config('DATABASE_URL')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = int(config('PORT'))
SECRET_KEY = config('SECRET_KEY').encode('utf-8')
