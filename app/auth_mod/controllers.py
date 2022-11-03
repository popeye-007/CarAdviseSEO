# flask dependencies
from flask import Blueprint, request, render_template, \
            flash, g, session, redirect, url_for

# password encryption tools 
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.auth_mod.forms import SigninForm
# Placeholder for users model
# from app. .models import Users


auth_mod = Blueprint('auth', __name__, url_prefix='auth')

# creating routes
@auth_mod.route('/signin/', methods=['GET', 'POST'])
def sigin():
    form = SigninForm(request.form)
    # verify that form submission
    if form.validate_on_submit():
        user = Users.query.filter

    return