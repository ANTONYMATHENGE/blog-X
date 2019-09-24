import os

from dotenv import load_dotenv as ld

ld()


class Config:
    debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vick:p@127.0.0.1:5432/blogx'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
