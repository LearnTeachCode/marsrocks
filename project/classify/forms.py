import string
from flask_wtf import Form
from wtforms import BooleanField

class ClassifyForm(Form):
    layered_rocks = BooleanField('layered_rocks', default=False,
        description='layered rocks')
    gypsum_vein = BooleanField('gypsum_vein', default=False,
        description='gypsum vein')
    bright_rocks = BooleanField('bright_rocks', default=False,
        description='bright rocks')
    meteorites = BooleanField('meteorites', default=False,
        description='meteorites')
    blueberries = BooleanField('blueberries', default=False,
        description='blueberries')
    wheel_wear = BooleanField('wheel_wear', default=False,
        description='wheel wear')
