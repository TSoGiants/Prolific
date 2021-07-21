from flask import Flask, Blueprint, render_template, redirect,session
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients, States, Zipcodes
from prolificApp.core.searchForm import Search
from prolificApp import db,app
from werkzeug.security import generate_password_hash



core_app = Blueprint('core', __name__)

@core_app.route('/')
def index():
	user = checkUser()
	return render_template('index.html', user = user)


@core_app.route('/about')
def about():
	user = checkUser()
	return render_template('About.html', user = user)
#creates endpoint for the About webpage


@core_app.route('/directory', methods= ('GET', 'POST'))
def directory():
	user = checkUser()
	form = Search()
	if form.validate_on_submit():
		
		fpsearch = form.name.data
		ssearch = form.state.data
		
		zsearch = form.zipcode.data
		statesearch = States.query.filter_by(states= ssearch).first()
		zipsearch = Zipcodes.query.filter_by(zipcode= zsearch).first()


		if statesearch != None:
			statesearch = statesearch.statesServed

		if zipsearch != None:	
			zipsearch = zipsearch.zipcodesServed
		

		''' ###############CODE TO CONSOLIDATE RESULTS#############
				create a variable called results, which will be a combination of statesearch and zipsearch '''
		
		#return render_template('results.html', statesearch = zipsearch) 
		return render_template('results.html', statesearch = statesearch, user = user, form = form) 
	


	return render_template('Directory2.html', form = form, user = user)

#creates endpoint for the directory webpage

@core_app.route('/food pantry profile')
def fpProfile():
	user = checkUser()
	return render_template('FoodPantryProfile.html', user = user)

#creates endpoint for the food pantry profile page webpage

def checkUser():
	if not session.get("currentUserID") is None:
			return FoodPantries.query.filter_by(foodpantries_id= session["currentUserID"]).first()
	else:
		return "none"

