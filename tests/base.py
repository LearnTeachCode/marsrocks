# TODO: remove most of this code once we can get app and db from project
from flask.ext.testing import TestCase
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

from app import app
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        # hash the plain text password before saving to database
        self.password = bcrypt.generate_password_hash(password)

    # required by flask-login
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.username)


# BaseTestCase creates settings that will be used in all tests
class BaseTestCase(TestCase):
    # create an instance of the flask app
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        # create all the database tables before each test
        db.create_all()
        db.session.add(User("admin", "password"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        # removes all tables after each test
        db.drop_all()
