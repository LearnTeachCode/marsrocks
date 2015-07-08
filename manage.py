import os
import unittest
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask import url_for

from project import app, db

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

# adds to ability to list routes using "$ python manage.py list_routes"
# http://flask.pocoo.org/snippets/117/
@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


# adds to ability to run tests using "$ python manage.py test"
@manager.command
def test():
    """Runs the unit tests without coverage."""

    # discover will look for tests inside the 'tests' folder
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
