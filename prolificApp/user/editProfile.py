from flask import Flask, Blueprint, render_template, redirect,flash,abort,session
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients
from prolificApp import db,app
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators, SelectField)
from wtforms.validators import DataRequired,Email,EqualTo
from prolificApp.user.models import FoodPantries, Clients
from werkzeug.security import check_password_hash


class Editprofile(FlaskForm):

    fpname = StringField('Food Pantry Name')
    fpemail = StringField("Food Pantry's Email",  validators = [Email()])
    fpcity = StringField('City')
    fpstate = SelectField("State", choices = ["Select State", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"])
    fpzipcode = StringField('Zipcode')
    fpstreet = StringField('Street Address')
    fpphone = StringField("Food Pantry's Phone Number")
    fpwebsite = StringField("Food Pantry's Website")
    fptimings = StringField("Time")
    fpinfoBring = StringField("Information Clients must bring")
    fpbio = StringField("Information about the food bank")
    submit = SubmitField('Finshed')



   