import os
from flask_sqlalchemy import SQLAlchemy
# Object based cofiguration file that will be used to set
# different configurations for different servers

class Config(object):
    TEST = False


class ProductionEnv(Config):
    # PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://<USER>:<pass>@<localhost>/<database>'
    DEBUG = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2
    CSRF_ENABLED     = True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    
class DevelopmentEnv(Config):
    # PostgreSQL
    DATABASE_URI = 'postgresql://<USER>:<pass>@<localhost>/<database>'