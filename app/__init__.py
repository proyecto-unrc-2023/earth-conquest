from flask import Flask
from config import config
from flask_cors import CORS

from app.backend.blueprints import games_bp

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"expire_on_commit": False})

def create_app(config_name="development"):
    # app stuff
    app = Flask(__name__)
    CORS(app)
    register_modules(app)

    # config stuff
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # db
    db.init_app(app)
    return app


# blueprints register
def register_modules(app):
    app.register_blueprint(games_bp, url_prefix='/games')
