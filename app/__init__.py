from logging import log
from flask import Flask
from flask_restful import Api

# Init Flask app
app = Flask(__name__)
api = Api(app)

from .models import login
login.init_app(app)
login.login_view = 'login'

from app import routes
app.register_blueprint(routes.cards)
app.register_blueprint(routes.user)
