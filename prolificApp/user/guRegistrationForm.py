from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,SubmitField,PasswordField,validators,SelectField)
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
import email_validator

#creates the registration form
class AddUser(FlaskForm):

	gufirst = StringField('First Name', validators = [DataRequired()])
	gulast = StringField("Last Name", validators = [DataRequired()])
	guemail = StringField('Email', validators = [DataRequired(),Email()])
	state = SelectField('State', validators = [DataRequired()], choices = ["Select State", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"])
	zipcode = IntegerField("Zipcode", validators = [DataRequired()])
	gupassword = PasswordField('Password', validators = [DataRequired(),EqualTo('guconfirm',message='Passwords must match!')])
	guconfirm = PasswordField('Confirm Password', validators = [DataRequired()])
	submit = SubmitField('Sign Up')


	def check_email(self, field):
        # Check if not None for that user email!
		if Clients.query.filter_by(fpemail=field.data).first():
			raise ValidationError('Your email has been registered already!')
