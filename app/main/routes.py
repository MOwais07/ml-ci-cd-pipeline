# app/main/routes.py

from flask import request, jsonify
from app.main import main
from app.main.model import predict

# Define the route for prediction
@main.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    result = predict(np.array(data['input']))
    return jsonify({"prediction": result.tolist()})

# Add two blank lines after class or function definitions
