import os

DATABASE = os.environ['DATABASE']
DATABASE_URL = os.environ['DATABASE_URL']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
SECRET_KEY = os.environ['SECRET_KEY'].encode('utf-8')
