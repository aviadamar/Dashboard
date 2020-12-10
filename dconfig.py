from decouple import config
import os


DATABASE = config('DATABASE')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
PORT = config('PORT')
SECRET_KEY = config('SECRET_KEY')
