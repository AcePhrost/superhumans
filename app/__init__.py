from flask import Flask

app = Flask(__name__)

from resources.characters import routes
from resources.users import routes


