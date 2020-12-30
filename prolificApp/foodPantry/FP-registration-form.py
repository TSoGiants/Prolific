from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     ,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class AddFoodPantry(FlaskForm):

	fpname = StringField('Food Pantry Name')
	fpemail = StringField("Food Pantry's Email")
	fpadress = StringField('Address')
	fpphone = StringField("Food Pantry's Phone Number")
	fpwebsite = StringField("Food Pantry's Website")
	fppassword = StringField('Password')
	fpconfirm = StringField('Confirm Password')
    submit = SubmitField('Sign Up')