from flask import Flask, Blueprint, render_template, redirect,flash,abort,session
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients
from prolificApp import db,app
from werkzeug.security import generate_password_hash,check_password_hash
from prolificApp.user.guRegistrationForm import AddUser
from prolificApp.user.fpRegistrationForm import AddFoodPantry
from prolificApp.user.fpLoginForm import fpLoginForm
from prolificApp.user.guLoginForm import guLoginForm
from flask_login import login_user,login_required,logout_user

user_app = Blueprint('Users', __name__)


#this route accepts info from form and checks database for users and anthencitates users
@user_app.route('/GUlogin', methods= ('GET', 'POST'))
def GUlogin():
	form = guLoginForm()
	if form.validate_on_submit():
		user = Clients.query.filter_by(guemail=form.email.data).first()
		if user.check_password(form.password.data) and user is not None:
			
			login_user(user)
			flash('Logged in successfully.')

	session['currently_logged_in'] = 'EMily'
	#return f"{session['currently_logged_in']}"
	return render_template('gulogin.html', form=form)

@user_app.route('/FPlogin', methods= ('GET', 'POST'))
def fplogin():
	form = fpLoginForm()
	if form.validate_on_submit():
		user = Clients.query.filter_by(fpemail=form.email.data).first()
		if user.check_password(form.password.data) and user is not None:
			login_user(user)
			flash('Logged in successfully.')

	return render_template('FPlogin.html', form=form)

@user_app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You logged out!' )
	return render_template('logout.html')


@user_app.route('/registerFP', methods= ('GET', 'POST'))
def registerFP():
	form = AddFoodPantry()

	if form.validate_on_submit():
		name = form.fpname.data
		email = form.fpemail.data
		address = form.fpaddress.data
		phone = form.fpphone.data
		website = form.fpwebsite.data
		password = (form.fppassword.data)

		new_food_pantry = FoodPantries(name, email, address, phone, website, password)
		db.session.add(new_food_pantry)
		db.session.commit()

		flash("Your account was created successfully!")

		return redirect(url_for('Users.FPeditprofile'))

	return render_template('registerFP.html', form = form)


@user_app.route('/registerGU', methods= ('GET', 'POST'))
def registerGU():
	form = AddUser()

	if form.validate_on_submit():
		first = form.gufirst.data
		last = form.gulast.data
		email = form.guemail.data
		state = form.state.data
		zipcode = form.zipcode.data
		password = generate_password_hash(form.gupassword.data)

		new_user = Clients(first, last, email, state, zipcode, password)
		db.session.add(new_user)
		db.session.commit()

		return redirect(url_for('Users.GUeditprofile'))

	return render_template('registerGU.html', form = form)


@user_app.route('/GUeditprofile', methods= ('GET', 'POST'))
def GUeditprofile():
	return render_template('GUeditprofile.html')




@user_app.route('/FPeditprofile', methods= ('GET', 'POST'))
def FPeditprofile():
	return render_template('FPeditprofile.html')


@user_app.route('/profile')
def profile():
	return render_template('profile.html')
