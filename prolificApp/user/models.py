from prolificApp import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash



#connects clients table to food pantry table
serves = db.Table('serves',
	db.Column('foodpantries_id', db.Integer, db.ForeignKey('food_pantries.foodpantries_id')),
    db.Column('clients_id', db.Integer, db.ForeignKey('clients.clients_id'))
    )
# database set up for food pantry info
class FoodPantries(db.Model, UserMixin):
	foodpantries_id = db.Column(db.Integer, primary_key=True)
	foodPantryName = db.Column(db.Text)
	FPemail = db.Column(db.String(64), unique=True,index=True)
	FPaddress = db.Column(db.Text)
	FPphone = db.Column(db.Text)
	FPwebsite = db.Column(db.Text)
	timings = db.Column(db.Text)
	infoBring = db.Column(db.Text)
	bio =db.Column(db.Text)
	FPpassword = db.Column(db.Text)


	serves = db.relationship('Clients', secondary=serves, backref= db.backref('statesServed', lazy = 'dynamic') )

	def __init__(self, foodPantryName, FPemail, FPaddress, FPphone, FPwebsite, timings, infoBring, bio, FPpassword ):
		self.foodPantryName = foodPantryName
		self.FPemail = FPemail 
		self.FPaddress = FPaddress
		self.FPphone = FPphone
		self.FPwebsite = FPwebsite
		self.timings = timings
		self.infoBring = infoBring
		self.bio = bio
		self.FPpassword = generate_password_hash(FPpassword)

	def check_password(self,password):
		return check_password_hash(self.password_hash,FPpassword)

	def __repr__(self):
		return f"The name of the food pantry is {self.foodPantryName}"


#set up client info database 
class Clients(db.Model, UserMixin):
	clients_id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.Text)
	lastName = db.Column(db.Text)
	GUemail = db.Column(db.String(64), unique=True,index=True)
	GUstate = db.Column(db.Text)
	GUzipcode = db.Column(db.Text)
	GUpassword = db.Column(db.Text)

	def __init__(self, firstName, lastName, GUemail, GUzipcode, GUstate, GUpassword ):
		self.firstName = firstName
		self.lastName = lastName
		self.GUemail = GUemail
		self.GUstate = GUstate
		self.GUzipcode = GUzipcode	
		self.GUpassword = generate_password_hash(GUpassword)       


	def check_password(self,password):
		return check_password_hash(self.password_hash,GUpassword)	

	def __repr__(self):
		return f"The client is {self.firstName} {self.lastName}" 