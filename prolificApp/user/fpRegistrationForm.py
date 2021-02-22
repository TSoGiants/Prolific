from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators,SelectField)
from wtforms.validators import DataRequired,Email,EqualTo



class AddFoodPantry(FlaskForm):

#text in quotes is the label for the input box
    fpname = StringField('Food Pantry Name', validators = [DataRequired()])
    fpemail = StringField("Food Pantry's Email", validators = [DataRequired(),Email()])
    fpcity = StringField('City', validators = [DataRequired()])
    fpstate = SelectField('State', validators = [DataRequired()], choices = ["Select State", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"])
    fpzipcode = StringField('Zipcode', validators = [DataRequired()])
    fpstreet = StringField('Street Address', validators = [DataRequired()])
    fpphone = StringField("Food Pantry's Phone Number", validators = [DataRequired()])
    fpwebsite = StringField("Food Pantry's Website")
    FPpassword = PasswordField('Password', validators = [DataRequired(),EqualTo("fpconfirm",message='Passwords must match!')])
    fpconfirm = PasswordField('Confirm Password', validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def check_email(self, field):
        # Check if not None for that user email!
        if FoodPantries.query.filter_by(fpemail=field.data).first():
            raise ValidationError('Your email has been registered already!')
