import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager

# create (instantiate) the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)

# create instance of login manager
login_manager = LoginManager()
# register login manager with the app object
login_manager.init_app(app)

# config
app.config.from_object(os.environ['APP_SETTINGS'])
print '== APP_SETTINGS:', os.environ['APP_SETTINGS']

#create SQLAlchemy object
db = SQLAlchemy(app)

# import blueprints
from project.users.views import users_blueprint

# register our blueprints with the app.
app.register_blueprint(users_blueprint)

from models import User

# define the login view
login_manager.login_view = "users.login"

# registers user_loader with flask-login.
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
