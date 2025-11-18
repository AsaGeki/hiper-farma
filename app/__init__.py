from flask import Flask
from app.routes import main
from app.routes import workers

def create_app():
    app = Flask(__name__)
    app.secret_key = "dev"

    app.register_blueprint(main)
    app.register_blueprint(workers, url_prefix="/workers")

    return app
