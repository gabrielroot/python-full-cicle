from flask import Blueprint
from .views.test import home

test = Blueprint('test', __name__)
test.add_url_rule('/', view_func=home, methods=['GET'])