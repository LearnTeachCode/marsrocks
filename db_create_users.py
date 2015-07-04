from project import db
from project.models import User

# insert data
db.session.add(User("admin", "ad@min.com", "password"))

# commit the changes
db.session.commit()
