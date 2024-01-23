from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.users_model import UserModel
from models.charactersModel import characterModels

from resources.users import bp as user_bp
api.register_blueprint(user_bp)

from resources.characters import bp as characters_bp
api.register_blueprint(characters_bp)


