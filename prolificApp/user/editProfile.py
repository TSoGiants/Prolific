from flask import Flask, Blueprint, render_template, redirect,flash,abort,session
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients
from prolificApp import db,app


class Editprofile(FlaskForm):

	fpname = StringField({{ result.foodPantryName }})
    fpemail = StringField({{ result.FPemail }},  validators = [Email()])
    fpcity = StringField({{ result.FPcity }})
    fpstate = SelectField({{ result.FPstate }}, choices = ["Select State", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"])
    fpzipcode = StringField({{ result.FPzipcode }})
    fpstreet = StringField({{ result.FPstreet }})
    fpphone = StringField({{ result.FPphone }})
    fpwebsite = StringField({{ result.fpwebsite }})
    fptimings = StringField({{ result.timings }})
    fpinfoBring = StringField({{ result.infoBring }})
    fpbio = StringField({{ result.bio }})


    submit = SubmitField('Finshed')