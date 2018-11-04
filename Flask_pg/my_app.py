from flask import Flask

from config import runtime_config
from api import api
from api.blu_view import pages_view
from db.db_creation import create_db
from db.db_app import db



def run_app():
    app = Flask(__name__)
    app.config.from_object(runtime_config())
    app.register_blueprint(api)
    app.register_blueprint(pages_view)
    app.secret_key = runtime_config().SECRET_KEY
    app.register_blueprint(create_db)
    db.init_app(app)

    return app
