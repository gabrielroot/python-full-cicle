import os
import logging.config

from flask import Flask
from decouple import config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    environment = config('APPLICATION_ENV', default='Development')
    app = Flask(__name__)
    config_name = f'training.config.{environment}'
    app.config.from_object(config_name)

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join(BASE_DIR, 'migrations'))

    logging.config.dictConfig(app.config['LOGGING'])
    logger.info('loading application with configuration {}'.format(config_name))

    register_blueprints(app)

    return app


def register_blueprints(app):
    from training.url import bp_v1

    app.register_blueprint(bp_v1)