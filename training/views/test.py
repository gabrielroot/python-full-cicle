from flask import jsonify
from flask.views import MethodView


class Home(MethodView):

    def get(self):
        data = {
            'status': 'ok'
        }
        return jsonify(data)
home = Home.as_view('home')