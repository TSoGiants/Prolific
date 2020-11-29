from flask import Flask, Blueprint, render_template

user_app = Blueprint('Users', __name__)

@user_app.route('/login')
def login():
	return render_template('login.html')
@user_app.route('/logout')
def logout():
	return render_template('logout.html')
@user_app.route('/registerFB')
def registerFB():
	return render_template('registerFB.html')
@user_app.route('/registerGU')
def registerGU():
	return render_template('registerGU.html')
@user_app.route('/profile')
def profile():
	return render_template('profile.html')
