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

''' 	#allData = Lawfirms.query.all()
	#return f"{allData}"

	#currentstate = States.query.filter_by(states= "Texas").first_or_404()
	#for x in currentstate:
		#return f"{x.states}"
	currentstate = States.query.get(3)
	#return f"{currentstate}"
	#test = currentstate.stateServed()
	#return f'{test}' 
	if request.method == 'POST':
		lfsearch = request.form["lawfirm"]
		ssearch = request.form["state"]
		#currentstate = States.query.filter_by(states= eachstate).first()
		statesearch = States.query.filter_by(states= ssearch).first().statesServed
		#statesearch = statesearch.statesServed
		#return redirect(url_for('Lawyer_Network.results', statesearch=statesearch))
		return render_template('directory.html', statesearch=statesearch)