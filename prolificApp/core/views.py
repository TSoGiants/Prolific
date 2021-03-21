from flask import Flask, Blueprint, render_template, redirect
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients, States
from prolificApp.core.searchForm import Search
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


@core_app.route('/directory', methods= ('GET', 'POST'))
def directory():
	form = Search()
	if form.validate_on_submit():
		#currentstate = FoodPantries.query.get(0)
		#currentstate = FoodPantries.query.all()[0]
		fpsearch = form.name.data
		ssearch = form.state.data
		zsearch = form.zipcode.data
		statesearch = States.query.filter_by(states= ssearch).first().statesServed
		zipsearch = FoodPantries.query.filter_by(FPzipcode= zsearch).first().zipcodesServed
		#pantrysearch = FoodPantries.query.filter_by(foodPantryName= fpsearch).first().serves
		#x = currentstate
		
		return render_template('results.html', statesearch = statesearch)
	'''currentstate = FoodPantries.query.get(3)
	if request.method == 'POST':
		fpsearch = request.form["foodpantries"]
		ssearch = request.form["FPstate"]
		zsearch = request.form['FPzipcode']
		statesearch = FoodPantries.query.filter_by(FPstate= ssearch).first().serves
		zipsearch = FoodPantries.query.filter_by(FPzipcode= zsearch).first().serves
		pantrysearch = FoodPantries.query.filter_by(foodPantryName= fpsearch).first().serves

		return render_template('Directory.html', statesearch=statesearch, zipsearch = zipsearch, pantrysearch= pantrysearch)'''


	return render_template('Directory2.html', form = form)

#creates endpoint for the directory webpage

@core_app.route('/food pantry profile')
def fpProfile():
	return render_template('FoodPantryProfile.html')

#creates endpoint for the food pantry profile page webpage

