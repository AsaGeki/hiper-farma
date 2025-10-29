from flask import Flask
from config import get_connection, get_s3_config

def create_app():
    app = Flask(__name__)
    from app.routes import main
    app.register_blueprint(main)

    return app
