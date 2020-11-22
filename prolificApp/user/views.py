from flask import Flask, Blueprint, render_template

user_app = Blueprint('Users', __name__)

@user_app.route('/login')
def login():
	return render_template('login.html')
@user_app.route('/logout')
def logout():
	return render_template('logout.html')	
@user_app.route('/register')
def register():
	return render_template('register.html')
@user_app.route('/profile')
def profile():
	return render_template('profile.html')	