from werkzeug.security import generate_password_hash,check_password_hash
#from flask_login import UserMixin
#from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators)
from wtforms.validators import DataRequired,Email,EqualTo


class fpLoginForm(FlaskForm):
    fpemail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
