import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'blog-db.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
