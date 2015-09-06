import random
from flask import render_template, Blueprint, request, redirect, url_for
from flask.ext.login import current_user
from sqlalchemy.sql.expression import func

from .forms import ClassifyForm
from project import db
from project.models import VisitedPhoto, Classification, Feature, Photo

# define blueprints
classify_blueprint = Blueprint(
    'classify', __name__,
    template_folder='templates'
)

def mark_photo_visited(random_img):
    visited_photo = VisitedPhoto(
        user_id = current_user.id,
        photo_id = random_img.id
    )
    db.session.add(visited_photo)
    db.session.commit()

# delete all items from visited photo for the current user
def clear_visited_photos():
    sql = 'delete from visited_photos where user_id =' + str(current_user.id)
    db.engine.execute(sql)

# count the number of photos not visited
def available_photos_count():
    return Photo.query.count() - VisitedPhoto.query.count()

def random_available_image():
    count = available_photos_count()
    # if there are 2 or more unvisited photos, show a random unvisited photo
    if count > 1:
        offset =  random.randrange(1, count)
    # if there is one 1 unvisited photo, show the photo
    elif count == 1:
        offset = 0
    # else delete all visited photos for the current user and show first image
    else:
        if current_user.is_authenticated():
            clear_visited_photos()
        offset = 0
    # select one photo that has not been visited
    sql = 'select id from photos where id not in (select photo_id from visited_photos) limit 1 offset ' + str(offset)
    return db.engine.execute(sql).first()

def classify_photo(request):
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

@classify_blueprint.route('/classify', methods = ['POST', 'GET'])
def index():
    # set up form
    error = None
    form = ClassifyForm(request.form)
    # grab random image that has not been visited
    random_img = random_available_image()

    if current_user.is_authenticated():
        template = 'classify.html'
        # mark current photo visited so the image won't be shown again
        mark_photo_visited(random_img)
    else:
        template = 'classify_static.html'

    if request.method == 'POST' and form.validate():
        # request.form contains a dictionary of all the fields in the form
        classify_photo(request)

    # render the template
    return render_template(template,
        current_user = current_user,
        form = form,
        error = error,
        photo = random_img
    )

