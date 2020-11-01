from flask import Flask, Blueprint

foodPantry_app = Blueprint('foodPantry', __name__)

@foodPantry_app.route('/')
def index():
	return "landing page"