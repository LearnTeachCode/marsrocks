import random
from flask import render_template, Blueprint, request, redirect, url_for
from flask.ext.login import current_user
from sqlalchemy.sql.expression import func

from .forms import ClassifyForm
from project import db
from project.models import Classification, Feature, Photo

# define blueprints
classify_blueprint = Blueprint(
    'classify', __name__,
    template_folder='templates'
)

def random_image():
    return db.session.query(Photo).order_by(func.random()).first()

@classify_blueprint.route('/classify', methods = ['POST', 'GET'])
def index():
    # set up form
    error = None
    form = ClassifyForm(request.form)

    if current_user.is_authenticated():
        template = 'classify.html'
    else:
        template = 'classify_static.html'

    if request.method == 'POST' and form.validate():
        # request.form contains a dictionary of all the fields in the form

        # fields: csrf_token, selected features, hidden photo_id.
        # loop all the fields.
        for field in request.form:
            # ignore csrf_token and photo_id fields
            if field != 'csrf_token' and field != 'photo_id':
                # find feature in the database
                feature = Feature.query.filter_by(slug=field).first()

                # create new classification object
                classification = Classification(
                    user_id = current_user.id,
                    feature_id = feature.id,
                    photo_id = request.form['photo_id']
                )

                # save to database
                db.session.add(classification)
                db.session.commit()

        # redirect after saving data
        return redirect(url_for('classify.index'))

    # render the template
    return render_template(template,
        current_user = current_user,
        form = form,
        error = error,
        photo = random_image()
    )

