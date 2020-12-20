from ProfilicApp import db

class Foodpantries(db.Model):
	foodPantry_id = db.Column(db.Integer, primary_key=True)
	foodPantryName = db.Column(db.Text)
	state = db.Column(db.Text)
    website = db.Column(db.Text)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)


def __init__(self, foodPantryName, state, website, phone, address )
