from flask.ext.testing import TestCase
from project import app, db
from project.models import User

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
