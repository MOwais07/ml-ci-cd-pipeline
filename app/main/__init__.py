# app/main/__init__.py

from flask import Blueprint

# Create the 'main' blueprint
main = Blueprint('main', __name__)

# Import routes
from . import routes  # Ensures routes are available to the blueprint