from flask import Flask, Blueprint, render_template

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
	return render_template('registerGU.html')
@user_app.route('/profile')
@user_app.route('/editprofile')
def editprofile():
	return render_template('editprofile.html')
def profile():
	return render_template('profile.html')
