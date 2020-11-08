from flask import Flask, Blueprint

foodPantry_app = Blueprint('foodPantry', __name__)

@foodPantry_app.route('/')
def index():
	return "landing page"
@foodPantry_app.route('/About')
def about():
	return "About"
@foodPantry_app.route('/Directory')
def directory():
	return "Directory"
@foodPantry_app.route('/Food pantry profile')

def fpProfile():
	return "Food pantry profile"

