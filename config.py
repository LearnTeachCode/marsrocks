import os

#default config
class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = '\xcb\x1e\xf3\x1b\xe4\xc6\x98?\x9c)\xc5i2C\x85\xf1\xf6\xd2\x90\x9b\x84\xf6\x05K'

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
