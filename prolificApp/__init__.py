from flask import Flask 

app = Flask(__name__)


from prolificApp.user.views import user_app
from prolificApp.foodPantry.views import foodPantry_app

app.register_blueprint(foodPantry_app)
app.register_blueprint(user_app)