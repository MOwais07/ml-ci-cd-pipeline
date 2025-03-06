# app/main/__init__.py

from flask import Blueprint
from .routes import some_route  # Fix the unused import issue by either using or removing the import

# Initialize the Blueprint
main = Blueprint('main', __name__)

# Add two blank lines after class or function definitions
