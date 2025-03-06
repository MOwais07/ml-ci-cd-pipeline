# app/main/__init__.py

from flask import Blueprint

# Initialize the Blueprint
main = Blueprint('main', __name__)

# Don't import routes here to avoid circular import
