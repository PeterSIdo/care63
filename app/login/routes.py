# app/login/routes
from flask import render_template
from app.login import bp

@bp.route('/login')
def login():
    return render_template('login/login.html', title='Login')