from flask_smorest import Blueprint

bp = Blueprint('users', __name__, description='Operations for users')

from . import routes