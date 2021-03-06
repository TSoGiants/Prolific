from flask import Flask
from sassutils.wsgi import SassMiddleware
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prolificApp.configs.config import db_uri
#from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)
app.wsgi_app = SassMiddleware(app.wsgi_app,{'prolificApp':("static/styles", "static/styles", "/static/styles")})
app.config['SECRET_KEY'] = 'mysecretkey'

from prolificApp.user.views import user_app
from prolificApp.core.views import core_app

#login_manager = LoginManager()
#login_manager.init_app(app)


app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Migrate(app,db)


app.register_blueprint(core_app)
app.register_blueprint(user_app)
