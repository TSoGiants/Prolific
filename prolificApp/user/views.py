from flask import Flask, Blueprint, render_template, redirect
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients
from prolificApp import db,app
from werkzeug.security import generate_password_hash
from prolificApp.user.guRegistrationForm import AddUser
from prolificApp.user.fpRegistrationForm import AddFoodPantry

user_app = Blueprint('Users', __name__)

@user_app.route('/login')
def login():
	return render_template('login.html')


@user_app.route('/logout')
def logout():
	return render_template('logout.html')


@user_app.route('/registerFP')
def registerFP():
	form = AddFoodPantry()

	if form.validate_on_submit():
		name = form.fpname.data
		email = form.fpemail.data
		address  = form.fpadress.data
		phone = form.fpphone.data
		website = form.fpwebsite.data
		password = generate_password_hash(form.password.data)

		new_food_pantry = FoodPantry(name, email, address, phone, website, password)
		db.session.add(new_food_pantry)
		db.session.commit()	

		return redirect(url_for('FPeditprofile'))		

	return render_template('registerFP.html', form = form)


@user_app.route('/registerGU')
def registerGU():
	FlaskForm = AddUser()

	if form.validate_on_submit():
		first = form.gufirst.data
		last = form.gulast.data
		email = form.guemail.data
		state = form.state.data
		zipcode = form.zipcode.data
		password = generate_password_hash(form.password.data) 

		new_user = User(first, last, email, state, zipcode, password)
		db.session.add(new_user)
		db.session.commit()	

		return redirect(url_for('GUeditprofile'))	

	return render_template('registerGU.html', form = form)


@user_app.route('/GUeditprofile')
def GUeditprofile():
	return render_template('GUeditprofile.html', form = form)


@user_app.route('/FPeditprofile')
def FPeditprofile():
	return render_template('FPeditprofile.html' form = form)	


@user_app.route('/profile')	
def profile():
	return render_template('profile.html')
