from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from models.user_model import UserModel
from models.characterModel import characterModels, users_model

from resources.user import bp as user_bp
api.register_blueprint(user_bp)

from resources.character import bp as characters_bp
api.register_blueprint(characters_bp)


