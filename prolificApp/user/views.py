from flask import Flask, Blueprint, render_template, redirect,flash,abort,session
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients, States, Zipcodes
from prolificApp import db,app
from werkzeug.security import generate_password_hash,check_password_hash
from prolificApp.user.guRegistrationForm import AddUser
from prolificApp.user.fpRegistrationForm import AddFoodPantry
from prolificApp.user.fpLoginForm import fpLoginForm
from prolificApp.user.guLoginForm import guLoginForm
from prolificApp.user.editProfile import Editprofile
from flask import request
#from flask_login import login_user,login_required,logout_user

user_app = Blueprint('Users', __name__)


#this route accepts info from form and checks database for users and anthencitates users
@user_app.route('/login', methods= ('GET', 'POST'))
def login():
	user = checkUser()
	form = fpLoginForm()

	if form.validate_on_submit():
		
		currentUser = FoodPantries.query.filter_by(FPemail=form.fpemail.data).first()
		#return f"{check_password_hash(user.GUpassword, form.password.data)}"
		#return f"{user.GUpassword} other one {generate_password_hash(form.password.data)}"
		#return f"{form.guemail.data}"
		#if user.check_password(form.password.data) and user is not None:

		#	login_user(user)
		#	flash('Logged in successfully.')
		session["currentUserID"] = currentUser.foodpantries_id
		return redirect(url_for('core.index'))
	return render_template('login.html', form=form, user = user)

@user_app.route('/FPlogin', methods= ('GET', 'POST'))
def fplogin():
	form = fpLoginForm()
	if form.validate_on_submit():
		user = Clients.query.filter_by(fpemail=form.email.data).first()
		if user.check_password(form.password.data) and user is not None:
			session["currentUserID"] = user.foodpantries_id
			flash('Logged in successfully.')

	return render_template('FPlogin.html', form=form)

@user_app.route('/logout')
def logout():
	user = checkUser()
	session.pop("currentUserID")
	user = "none"
	flash('You logged out!' )
	return render_template('logout.html', user = user)


@user_app.route('/registerFP', methods= ('GET', 'POST'))
def registerFP():
	form = AddFoodPantry()
	user = "none"
	if form.validate_on_submit():
		name = form.fpname.data
		email = form.fpemail.data
		street = form.fpstreet.data
		city = form.fpcity.data
		state = form.fpstate.data
		zipcode = form.fpzipcode.data #we'll use zipcode to create entry in zipcode table
		phone = form.fpphone.data
		website = form.fpwebsite.data
		timings = ''
		infoBring = ''
		bio = ''
		FPpassword = form.FPpassword.data

		#creating new zipcode entry
		zipcodeFP = Zipcodes.query.filter_by(zipcode = zipcode).first()
		if zipcodeFP == None:# If the zipcode entered by user is not in table, create zipcode entry
			new_zipcode = Zipcodes(zipcode)
			db.session.add(new_zipcode)
			db.session.commit()


		new_food_pantry = FoodPantries(name, email, street, city, phone, website,timings, infoBring, bio, FPpassword)
		db.session.add(new_food_pantry)
		db.session.commit()

		#create new state entry
		stateFP = States.query.filter_by(states = state).first()
		if stateFP == None: #if the state entered by user is not in table, create a new entry
			newState = States(state)
			db.session.add(newState)
			db.session.commit()

		##add the states association
		currentFP = FoodPantries.query.filter_by(FPemail = email).first()
		#return f"{currentFP.FPemail}"
		currentState = States.query.filter_by(states= state).first() #search the states table for the state that was just entered
		if currentState != None:
			currentState.statesServed.append(currentFP)
			db.session.commit()
		#add in zipcode association
		currentZipcode= Zipcodes.query.filter_by(zipcode= zipcode).first() #search the zipcodes table for the zipcode that was just entered
		if currentZipcode != None:
			currentZipcode.zipcodesServed.append(currentFP)
			db.session.commit()

		session["currentUserID"] = currentFP.foodpantries_id
		return render_template('GUeditprofile.html',user = currentFP)


	return render_template('registerFP.html', form = form, user = user )


@user_app.route('/registerGU', methods= ('GET', 'POST'))
def registerGU():
	form = AddUser()

	if form.validate_on_submit():
		first = form.gufirst.data
		last = form.gulast.data
		email = form.guemail.data
		state = form.state.data
		zipcode = form.zipcode.data
		#password = generate_password_hash(form.gupassword.data)
		password = form.gupassword.data
		new_user = Clients(first, last, email, zipcode,state, password)
		db.session.add(new_user)
		db.session.commit()

		#store who is logged in in the session object
		session["currentUser"] = Clients.query.filter_by(GUemail = email).first().clients_id


		return redirect(url_for('Users.GUeditprofile'))

	return render_template('registerGU.html', form = form)


@user_app.route('/editprofile', methods= ('GET', 'POST'))
def editprofile():
	#create edit profile form
	#replace html code in editprofile.html using the jinja template
	#pulling information from the form in this route
	#update the database
	form = Editprofile()
	if form.validate_on_submit():
		name = form.fpname.data
		email = form.fpemail.data
		street = form.fpstreet.data
		city = form.fpcity.data
		state = form.fpstate.data
		zipcode = form.fpzipcode.data
		phone = form.fpphone.data
		website = form.fpwebsite.data
		timings = form.fptimings.data
		infoBring = form.fpinfoBring.data
		bio = form.fpbio.data
		update = FoodPantries(name, email, street, city, state, zipcode, phone, website, timings, infoBring, bio)
		db.session.add(update)
		db.session.commit()
	

	user = checkUser()
	return render_template('editprofile.html', user = user, form = form)




@user_app.route('/FPeditprofile', methods= ('GET', 'POST'))
def FPeditprofile():
	user = checkUser()
	return render_template('FPeditprofile.html', user = user)


@user_app.route('/profile')
def profile():
	user = checkUser()

	return render_template('profile.html', user = user)

@user_app.route('/test')
def test():
	x = checkUser().FPemail
	return f"{x}"

def checkUser():
	if not session.get("currentUserID") is None:
			return FoodPantries.query.filter_by(foodpantries_id= session["currentUserID"]).first()
	else:
		return "none"
