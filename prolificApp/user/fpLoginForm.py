from werkzeug.security import generate_password_hash,check_password_hash
#from flask_login import UserMixin
#from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,PasswordField,validators)
from wtforms.validators import DataRequired,Email,EqualTo
from prolificApp.user.models import FoodPantries, Clients
from werkzeug.security import check_password_hash


class fpLoginForm(FlaskForm):
    fpemail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate(self): #this is the method that validates the form
        
        rv = FlaskForm.validate(self) #checks if the data was input
        if not rv:
            return False #validation didnt pass 

        #check if the email entered is actually in database
        user = FoodPantries.query.filter_by(FPemail=self.fpemail.data).first()

        if user: #this will be false if the above query returned nothing
            #return True
            #if it is true this code will run
            if not check_password_hash(user.FPpassword, self.password.data): #comparing databse password with form password
                self.password.errors.append("Incorrect email or password")
                return False

            return True
        else:
            self.password.errors.append("Incorrect email or password")
            return False
