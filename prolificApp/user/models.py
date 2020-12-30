from prolificApp import db

#connects clients table to food pantry table
serves = db.Table('serves',
	db.Column('foodpantries_id', db.Integer, db.ForeignKey('food_pantries.foodpantries_id')),
    db.Column('clients_id', db.Integer, db.ForeignKey('clients.clients_id'))
    )
# database set up for food pantry info
class FoodPantries(db.Model):
	foodpantries_id = db.Column(db.Integer, primary_key=True)
	foodPantryName = db.Column(db.Text)
	FPemail = db.Column(db.Text)
	FPaddress = db.Column(db.Text)
	FPphone = db.Column(db.Text)
	FPwebsite = db.Column(db.Text)
	timings = db.Column(db.Text)
	infoBring = db.Column(db.Text)
	bio =db.Column(db.Text)


serves = db.relationship('CLients', secondary=serves, backref= db.backref('statesServed', lazy = 'dynamic') )

def __init__(self,foodPantryName, FPemail, FPaddress, FPphone, FPwebsite, timings, infoBring, bio ):
	self.foodPantryName = foodPantryName
	self.FPemail = FPemail 
	self.FPaddress = FPaddress
	self.FPphone = FPphone
	self.FPwebsite = FPwebsite
	self.timings = timings
	self.infoBring = infoBring
	self.bio = bio

	def __repr__(self):
		return f"The name of the food pantry is {self.foodPantryName}"


#set up client info database 
class Clients(db.Model):
	clients_id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.Text)
	lastName = db.Column(db.Text)
	GUemail = db.Column(db.Text)
	GUstate = db.Column(db.Text)
	GUzipcode = db.Column(db.Text)

def __init__(firstName, lastName, GUemail, GUzipcode, GUstate ):
	self.firstName = firstName
	self.lastName = lastName
	self.GUemail = GUemail
	self.GUstate = GUstate
	self.GUzipcode = GUzipcode	       

	def __repr__(self):
		return f"The client is {self.firstName} {self.lastName}" 