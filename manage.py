import os
import unittest
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db

# config
try:
    app.config.from_object(os.environ['APP_SETTINGS'])
except:
    app.config.from_object('config.DevelopmentConfig')

# create migration instance
migrate = Migrate(app, db)

# create manager instance
manager = Manager(app)

# run migration from the commandline use 'db'
manager.add_command('db', MigrateCommand)

# adds to ability to run tests using "$ python manage.py test"
@manager.command
def test():
    """Runs the unit tests without coverage."""

    # discover will look for tests inside the 'tests' folder
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
