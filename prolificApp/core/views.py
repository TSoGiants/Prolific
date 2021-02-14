from flask import Flask, Blueprint, render_template, redirect
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients
from prolificApp import db,app
from werkzeug.security import generate_password_hash



core_app = Blueprint('core', __name__)

@core_app.route('/')
def index():
	return render_template('index.html')


@core_app.route('/about')
def about():
	return render_template('About.html')
#creates endpoint for the About webpage


@core_app.route('/directory')
def directory():
	return render_template('Directory.html')
#creates endpoint for the directory webpage

@core_app.route('/food pantry profile')
def fpProfile():
	return render_template('FoodPantryProfile.html')

#creates endpoint for the food pantry profile page webpage

