from flask import render_template, Blueprint

# define blueprints
about_blueprint = Blueprint(
    'about', __name__,
    template_folder='templates'
)

@about_blueprint.route('/')
def index():
    return render_template('about.html')
