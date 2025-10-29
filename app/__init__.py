from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Aqui você pode inicializar banco, boto3 etc
    # db.init_app(app)
    # s3_client = boto3.client(...)

    # Registrar blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
