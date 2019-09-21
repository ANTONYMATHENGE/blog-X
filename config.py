import os

from dotenv import load_dotenv as ld

ld()


class Config:
    debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
