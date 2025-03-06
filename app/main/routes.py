from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


# Define a root route
@main.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask App!"})


# Your existing prediction route
@main.route("/predict", methods=["POST"])
def predict():
    data = [1, 2, 3]  # Example data, replace with actual logic
    result = [x * 2 for x in data]
    return jsonify({"prediction": result})
