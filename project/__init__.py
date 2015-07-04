import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

# create (instantiate) the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)

# config
app.config.from_object(os.environ['APP_SETTINGS'])
print '=== APP_SETTINGS:', os.environ['APP_SETTINGS']

#create SQLAlchemy object
db = SQLAlchemy(app)
