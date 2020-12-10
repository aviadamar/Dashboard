import os
# from decouple import config

# DATABASE = config('DATABASE')
# DATABASE_URL = config('DATABASE_URL')
# USER = config('USER')
# PASSWORD = config('PASSWORD')
# HOST = config('HOST')
# PORT = int(config('PORT'))
# SECRET_KEY = config('SECRET_KEY').encode('utf-8')

DATABASE = os.environ['DATABASE']
DATABASE_URL = os.environ['DATABASE_URL']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
SECRET_KEY = os.environ['SECRET_KEY'].encode('utf-8')
