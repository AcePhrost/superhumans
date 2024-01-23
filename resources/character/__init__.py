from flask_smorest import Blueprint

bp = Blueprint('characters',__name__, description='Ops on characters', url_prefix='/characters')

from . import routes