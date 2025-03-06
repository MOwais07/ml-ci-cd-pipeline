# app/__init__.py

from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

from app.main import main

app.register_blueprint(main)

# Add two blank lines before the end of the file
