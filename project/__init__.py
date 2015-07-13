import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from shared.global_variables import get_current_year

# create (instantiate) the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)

# create instance of login manager
login_manager = LoginManager()
# register login manager with the app object
login_manager.init_app(app)

# config
try:
    app.config.from_object(os.environ['APP_SETTINGS'])
except:
    app.config.from_object('config.DevelopmentConfig')

#create SQLAlchemy object
db = SQLAlchemy(app)

# import blueprints
from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.about.views import about_blueprint
from project.stats.views import stats_blueprint
from project.classify.views import classify_blueprint
from project.features.views import features_blueprint

# register our blueprints with the app.
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(stats_blueprint)
app.register_blueprint(classify_blueprint)
app.register_blueprint(features_blueprint)

# register variables used in base template
app.context_processor(get_current_year)


from models import User

# define the login view
login_manager.login_view = "users.login"

# registers user_loader with flask-login.
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
