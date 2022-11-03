from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo


class SigninForm(FlaskForm):
    email = EmailField('Email',[Email(message='You need to enter your email')])
    password = PasswordField('Password',[DataRequired(message='You need to enter your email')])