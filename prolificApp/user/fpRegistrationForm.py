from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators)
from wtforms.validators import DataRequired,Email,EqualTo



class AddFoodPantry(FlaskForm):

#text in quotes is the label for the input box
    fpname = StringField('Food Pantry Name', validators = [DataRequired()])
    fpemail = StringField("Food Pantry's Email", validators = [DataRequired(),Email()])
    fpaddress = StringField('Address', validators = [DataRequired()])
    fpphone = StringField("Food Pantry's Phone Number", validators = [DataRequired()])
    fpwebsite = StringField("Food Pantry's Website")
    fppassword = PasswordField('Password', validators = [DataRequired(),EqualTo("fpconfirm",message='Passwords must match!')])
    fpconfirm = PasswordField('Confirm Password', validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def check_email(self, field):
        # Check if not None for that user email!
        if FoodPantries.query.filter_by(fpemail=field.data).first():
            raise ValidationError('Your email has been registered already!')

     
