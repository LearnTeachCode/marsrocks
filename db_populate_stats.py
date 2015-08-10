import datetime

from project import db
from project.models import Photo, Feature
from project.users.models import User
from project.classify.models import Classification

db.drop_all()
db.create_all()

db.session.add(Feature('layered rocks', 'features/layered_rock.jpg', 'layered_rocks'))
db.session.add(Feature('gypsum vein', 'features/gypsum_vein.jpg', 'gypsum_vein'))
db.session.add(Feature('bright rocks', 'features/bright_rocks.jpg', 'bright_rocks'))
db.session.add(Feature('meteorites', 'features/meteorites.jpg', 'meteorites'))
db.session.add(Feature('blueberries', 'features/blueberries.jpg', 'blueberries'))
db.session.add(Feature('wheel wear', 'features/wheel_wear.jpg', 'wheel_wear'))


db.session.add(User('user1', 'password'))
db.session.add(User('user2', 'password'))
db.session.add(User('user3', 'password'))
db.session.add(User('user4', 'password'))
db.session.add(User('user5', 'password'))
db.session.commit()


db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/00774/opgs/edr/fcam/FLB_466197342EDR_F0421020FHAZ00323M_.JPG', 'photo1', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/msss/00774/mhli/0774MH0003120010300255C00_DXXX.jpg', 'photo2', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/msss/00000/mrdi/0000MD0000000000100375C00_DXXX.jpg', 'photo3', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/msss/00774/mhli/0774MH0002580000300260S00_DXXX.jpg', 'photo4', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/msss/00000/mrdi/0000MD0000000000101032E01_DXXX.jpg', 'photo5', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/00674/opgs/edr/fcam/FRB_457337027EDR_F0380012FHAZ00340M_.JPG', 'photo6', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/00674/opgs/edr/rcam/RLB_457337150EDR_F0380018RHAZ00331M_.JPG', 'photo7', datetime.datetime.now() ))
db.session.add(Photo('http://mars.jpl.nasa.gov/msl-raw-images/msss/00000/mrdi/0000MD0000000000101504C00_DXXX.jpg', 'photo8', datetime.datetime.now() ))
db.session.commit()

db.session.add(Classification( 1, 1, 1))
db.session.add(Classification( 1, 1, 2))
db.session.add(Classification( 2, 1, 1))
db.session.add(Classification( 2, 1, 2))
db.session.add(Classification( 3, 1, 5))

db.session.add(Classification( 3, 2, 5))
db.session.add(Classification( 4, 2, 5))
db.session.add(Classification( 5, 2, 5))

db.session.add(Classification( 1, 3, 5))
db.session.add(Classification( 2, 3, 5))
db.session.add(Classification( 3, 3, 5))
db.session.add(Classification( 4, 3, 5))
db.session.add(Classification( 4, 3, 3))
db.session.add(Classification( 5, 3, 5))

db.session.add(Classification( 3, 4, 5))
db.session.add(Classification( 1, 4, 5))
db.session.add(Classification( 1, 4, 4))
db.session.add(Classification( 1, 4, 3))
db.session.add(Classification( 2, 4, 5))
db.session.add(Classification( 2, 4, 4))
db.session.add(Classification( 2, 4, 3))

db.session.add(Classification( 3, 5, 1))
db.session.add(Classification( 3, 5, 2))
db.session.add(Classification( 3, 5, 3))
db.session.add(Classification( 3, 5, 4))
db.session.add(Classification( 3, 5, 5))
db.session.add(Classification( 3, 5, 6))
db.session.add(Classification( 4, 5, 1))
db.session.add(Classification( 4, 5, 2))
db.session.add(Classification( 4, 5, 3))
db.session.add(Classification( 4, 5, 4))
db.session.add(Classification( 4, 5, 5))
db.session.add(Classification( 4, 5, 6))
db.session.add(Classification( 5, 5, 1))
db.session.add(Classification( 5, 5, 2))
db.session.add(Classification( 5, 5, 3))
db.session.add(Classification( 5, 5, 4))
db.session.add(Classification( 5, 5, 5))
db.session.add(Classification( 5, 5, 6))


db.session.add(Classification( 1, 6, 4))
db.session.add(Classification( 1, 6, 5))
db.session.add(Classification( 2, 6, 1))
db.session.add(Classification( 2, 6, 2))

db.session.add(Classification( 1, 7, 3))
db.session.add(Classification( 2, 7, 3))
db.session.add(Classification( 3, 7, 3))
db.session.add(Classification( 4, 7, 3))
db.session.add(Classification( 5, 7, 3))

db.session.add(Classification( 1, 8, 1))
db.session.add(Classification( 2, 8, 2))
db.session.add(Classification( 3, 8, 3))
db.session.add(Classification( 4, 8, 4))
db.session.add(Classification( 5, 8, 5))

db.session.commit()
