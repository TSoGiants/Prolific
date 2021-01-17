from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,SubmitField,PasswordField,validators)
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
import email_validator

#creates the registration form
class AddUser(FlaskForm):

	gufirst = StringField('First Name', validators = [DataRequired()])
	gulast = StringField("Last Name", validators = [DataRequired()])
	guemail = StringField('Email', validators = [DataRequired(),Email()])
	state = StringField("State", validators = [DataRequired()])
	zipcode = IntegerField("Zipcode", validators = [DataRequired()])
	gupassword = PasswordField('Password', validators = [DataRequired(),EqualTo('guconfirm',message='Passwords must match!')])
	guconfirm = PasswordField('Confirm Password', validators = [DataRequired()])
	submit = SubmitField('Sign Up')


	def check_email(self, field):
        # Check if not None for that user email!
		if Clients.query.filter_by(fpemail=field.data).first():
			raise ValidationError('Your email has been registered already!')