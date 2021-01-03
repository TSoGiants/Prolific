from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,SubmitField,validators)
from wtforms.validators import DataRequired



#creates the registration form
class AddUser(FlaskForm):

	gufirst = StringField('First Name')
	gulast = StringField("Last Name")
	guemail = StringField('Email')
	state = StringField("State")
	zipcode = IntegerField("Zipcode")
	gupasword = StringField('Password')
	guconfirm = StringField('Confirm Password')
	submit = SubmitField('Sign Up')