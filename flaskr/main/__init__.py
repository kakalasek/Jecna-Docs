from flask import Blueprint

main_page = Blueprint('main_page', __name__, template_folder='templates')

from . import routes, events