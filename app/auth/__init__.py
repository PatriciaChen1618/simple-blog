"""make the auth blueprint"""

from flask import Blueprint


auth = Blueprint('auth', __name__)  # name, import_name

from . import views