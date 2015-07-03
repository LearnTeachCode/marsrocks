from flask.ext.testing import TestCase

from app import app

# BaseTestCase creates settings that will be used in all tests
class BaseTestCase(TestCase):
    """A base test case."""

    # create an instance of the flask app
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app
