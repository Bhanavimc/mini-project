from flask import Flask
from .routes import main
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)  # Initialize SQLAlchemy with the app

      # Load configurations from config.py
    app.register_blueprint(main)      # Register the routes blueprint

    return app

