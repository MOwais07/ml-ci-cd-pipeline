from flask import Flask
from app.main.routes import main

app = Flask(__name__)

app.register_blueprint(main)  # Register the blueprint
