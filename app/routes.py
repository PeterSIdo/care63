from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title='Home')

def init_app(app):
    app.register_blueprint(main)