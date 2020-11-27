from flask import Flask
from decouple import config


def create_app():
    environment = config('APPLICATION_ENV', default='Development')
    app = Flask(__name__)
    config_name = f'training.config.{environment}'
    app.config.from_object(config_name)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from training.url import test

    app.register_blueprint(test)