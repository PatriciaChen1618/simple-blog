from flask import Blueprint


# make main blueprint
main = Blueprint('main', __name__)

from . import views, errors
