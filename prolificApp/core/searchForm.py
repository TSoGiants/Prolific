from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,SubmitField,PasswordField,validators,SelectField)
from wtforms.validators import DataRequired,Email,EqualTo

class Search(FlaskForm):
	state = SelectField('State', validators = [DataRequired()], choices = ["Select State",'Arizona','California','Florida','Georgia'])
	submit = SubmitField('Sign Up')

	def validate(self): #this is the method that validates the form
		rv = FlaskForm.validate(self) #checks if the data was input

		if not rv:
			return False
		else:	 #validation didnt pass 
			return True