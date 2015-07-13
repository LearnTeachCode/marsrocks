#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'This is the local insecure secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///marsrocks.db'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    # use sqlite in memory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # devs can customize the database by setting the environment variable

class ProductionConfig(BaseConfig):
    DEBUG = False
