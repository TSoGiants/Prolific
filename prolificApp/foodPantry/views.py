from flask import Flask, Blueprint

foodPantry_app = Blueprint('foodPantry', __name__)

@foodPantry_app.route('/')
def index():
	return "landing page"
@foodPantry_app.route('/About')
def index():
	return "About"
@foodPantry_app.route('/Directory')
def index():
	return "Directory"
@foodPantry_app.route('/Food pantry profile')
def index():
	return "Food pantry profile"

