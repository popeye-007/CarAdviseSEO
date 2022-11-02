import os
from flask_sqlalchemy import SQLAlchemy
# Object based cofiguration file that will be used to set
# different configurations for different servers

class Config(object):
    TESTING = False
    DB_SERVER = 'localhost'
    DB_NAME = 'carAdviseSum'
    DB_USER = 'postgre'
    DB_PASS = 'postgresql'
    DEBUG = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2
    CSRF_ENABLED     = True
    # Generate Random keys using python -c 'import secrets; print(secrets.token_hex())'
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"

    @property
    def db_connection(self):
        SQLALCHEMY_DATABASE_URI = f'postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_SERVER}/{self.DB_NAME}'
        return SQLALCHEMY_DATABASE_URI

class PRODENV(Config):
    DB_SERVER = ''
    DB_NAME = ''
    DB_USER = ''
    DB_PASS = ''
    # Generate Random keys using python -c 'import secrets; print(secrets.token_hex())'
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    
class DEVENV(Config):
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_SESSION_KEY = "an01her_1#s1_v@lu3"
    SECRET_KEY = "an0ther_D3V_v@lu3"

class TESTINGENV(Config):
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'