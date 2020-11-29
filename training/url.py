from flask import Blueprint
from .views.test import home

bp_v1 = Blueprint('test', __name__, url_prefix='/api/v1')
bp_v1.add_url_rule('/', view_func=home, methods=['GET'])