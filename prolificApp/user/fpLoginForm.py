from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager

@login_manager.user_loader
def load_user(user_id)
	return FoodPantries.query.get(user_id)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


hashed_pass = generate_password_hash("mypassword")

login_manager = LoginManager()

login_manager.init