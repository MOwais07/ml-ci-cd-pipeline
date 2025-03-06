# app/__init__.py

from flask import Flask
from app.main import main

# Initialize the Flask app
app = Flask(__name__)

app.register_blueprint(main)

# Add two blank lines before the end of the file
