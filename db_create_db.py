from project import db
from project.models import Feature

db.drop_all()
db.create_all()

# insert data
db.session.add(Feature('layered rocks', 'features/layered_rock.jpg'))
db.session.add(Feature('gypsum vein', 'features/gypsum_vein.jpg'))
db.session.add(Feature('bright rocks', 'features/bright_rocks.jpg'))
db.session.add(Feature('meteorites', 'features/meteorites.jpg'))
db.session.add(Feature('blueberries', 'features/blueberries.jpg'))
db.session.add(Feature('wheel wear', 'features/wheel_wear.jpg'))

# commit the changes
db.session.commit()
