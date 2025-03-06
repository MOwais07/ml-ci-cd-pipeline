# app/main/routes.py

from . import main

# Define the routes for the 'main' blueprint
@main.route('/')
def index():
    return "Hello, World!"