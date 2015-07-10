import random
from flask import render_template, Blueprint, request, redirect, url_for
from flask.ext.login import current_user

from .forms import ClassifyForm
from project import db
from project.models import Classification, Feature

# define blueprints
classify_blueprint = Blueprint(
    'classify', __name__,
    template_folder='templates'
)

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
        #  loop through the post data
        for field in request.form:
            if field != 'csrf_token':
                # find feature in the database
                feature = Feature.query.filter_by(slug=field).first()
                # create new classification object
                classification = Classification(
                    user_id = current_user.id,
                    feature_id = feature.id,
                    photo_id = random.randrange(1, 10)
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
        error = error
    )
