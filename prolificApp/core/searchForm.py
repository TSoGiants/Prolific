from flask_wtf import FlaskForm
from wtforms import (StringField,IntegerField,SubmitField,PasswordField,validators,SelectField)
from wtforms.validators import DataRequired,Email,EqualTo

class Search(FlaskForm):
	name = StringField('Food Pantry')
	zipcode = StringField('Zipcode')
	state = SelectField('State', choices = ["Select State", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"])
	submit = SubmitField('Search')

	def validate(self): #this is the method that validates the form
		rv = FlaskForm.validate(self) #checks if the data was input

		if not rv:
			return False
		else:	 #validation didnt pass 
			return True