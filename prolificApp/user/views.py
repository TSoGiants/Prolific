from flask import Flask, Blueprint, render_template, redirect
from flask import url_for
from flask import send_from_directory
from flask import request
import os
from prolificApp.user.models import FoodPantries, Clients
from prolificApp import db,app


user_app = Blueprint('Users', __name__)

@user_app.route('/login')
def login():
	return render_template('login.html')
@user_app.route('/logout')
def logout():
	return render_template('logout.html')
@user_app.route('/registerFP')
def registerFP():
	return render_template('registerFP.html')

@user_app.route('/registerGU')
def registerGU():
	FlaskForm = AddUser()
	


	return render_template('registerGU.html')





@user_app.route('/editprofile')
def editprofile():
	return render_template('editprofile.html')

@user_app.route('/profile')	
def profile():
	return render_template('profile.html')
