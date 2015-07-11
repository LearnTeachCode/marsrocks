import os

#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'This is the local insecure secret'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    # use sqlite in memory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # :memory: doesn't work on travis even if I set testing.db in settings.
    # must set testing.db here for travis to pass
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # devs can customize the database by setting the environment variable
    try:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        print '== os DATABASE_URL:'
    # default is to use sqlite
    except:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///marsrocks.db'
        print '== sqlite'

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
