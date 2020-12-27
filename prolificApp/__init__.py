from flask import Flask
from sassutils.wsgi import SassMiddleware
app = Flask(__name__)
app.wsgi_app = SassMiddleware(app.wsgi_app,{'prolificApp':("static/styles", "static/styles", "/static/styles")})

from prolificApp.user.views import user_app
from prolificApp.foodPantry.views import foodPantry_app

app.register_blueprint(foodPantry_app)
app.register_blueprint(user_app)
