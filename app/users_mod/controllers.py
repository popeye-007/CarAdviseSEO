# Flask dependencies
from flask import Blueprint, g, redirect, url_for, \
    session, flash, request, render_template
# password hashing
from werkzeug.security import generate_password_hash
# Get created forms
from app.users_mod.forms import CreateUserForm
# Get created DB models
from app.users_mod.models import Users
from app import db

users_mod = Blueprint('users', __name__, url_prefix='/users')

@users_mod.route('/users', methods=['GET', 'POST'])
def get_all_users():
    users = db.session.execute(db.select(Users).order_by(Users.name)).scalars()

    return render_template('users/userslist.html', users=users)
    
@users_mod.route('/create', methods=['GET', 'POST'])
def create_new_user():
    if request.method == 'POST':
        user = Users(
            name = request.form['username'],
            email = request.form['email'],
            password = request.form['password'],
            is_active = request.form['is_active']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('get_user_details', id=user.id))

    return render_template('users/userscreate.html')

@users_mod.route('/details/<int:id>', methods=['GET'])
def get_user_details(id):
    user = db.get_or_404(Users, id)
    return render_template('users/userdetails.html')
