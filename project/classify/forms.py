import string
from flask_wtf import Form
from wtforms import BooleanField
from wtforms.validators import Optional

class ClassifyForm(Form):
    layered_rocks = BooleanField('layered_rocks', default=False,
        description='layered rocks', validators=[Optional()])
    gypsum_vein = BooleanField('gypsum_vein', default=False,
        description='gypsum vein', validators=[Optional()])
    bright_rocks = BooleanField('bright_rocks', default=False,
        description='bright rocks', validators=[Optional()])
    meteorites = BooleanField('meteorites', default=False,
        description='meteorites', validators=[Optional()])
    blueberries = BooleanField('blueberries', default=False,
        description='blueberries', validators=[Optional()])
    wheel_wear = BooleanField('wheel_wear', default=False,
        description='wheel wear', validators=[Optional()])

    # custom validations
    # http://stackoverflow.com/questions/29703979/flask-conditional-validation-on-multiple-form-fields
    def validate(self):
        #validate that at least one feature is selected
        at_least_one_filled =  self.layered_rocks.data or self.gypsum_vein.data \
            or self.bright_rocks.data or self.meteorites.data \
            or self.blueberries.data or self.wheel_wear.data

        # run the default validations
        if not super(ClassifyForm, self).validate():
            return False
        # run custom validation
        if not at_least_one_filled:
            msg = 'At least one feature must be selected'
            self.layered_rocks.errors.append(msg)
            return False
        return True
