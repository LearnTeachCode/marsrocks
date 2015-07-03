import os
import unittest

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app

# config
app.config.from_object(os.environ['APP_SETTINGS'])

# create manager instance
manager = Manager(app)

# adds to ability to run tests using "$ python manage.py test"
@manager.command
def test():
    """Runs the unit tests without coverage."""

    # discover will look for tests inside the 'tests' folder
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
