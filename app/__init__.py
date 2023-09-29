from flask import Flask
from config import config


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
