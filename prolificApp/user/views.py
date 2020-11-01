from flask import Flask, Blueprint

user_app = Blueprint('Users', __name__)

@user_app.route('/login')
def login():
	return "login Page"