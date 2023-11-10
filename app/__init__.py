from flask import Flask
from config import config
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from app.backend.api import games_bp


def create_app(config_name="development"):
    # app stuff
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    register_modules(app)

    # config stuff
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    return app


# api register
def register_modules(app):
    app.register_blueprint(games_bp, url_prefix='/games')
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


# swagger stuff
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "earth-conquest"
    }
)
