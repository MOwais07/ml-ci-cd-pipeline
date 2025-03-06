# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints here
    from app.main import main
    app.register_blueprint(main)

    return app