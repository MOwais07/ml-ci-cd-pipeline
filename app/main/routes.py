# app/main/routes.py

from flask import request, jsonify
from app.main.model import predict
from app import app
from app.main import main

@main.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    result = predict(np.array(data['input']))
    return jsonify({"prediction": result.tolist()})
