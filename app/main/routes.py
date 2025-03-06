from flask import Blueprint, request, jsonify
from app.main.model import predict

main = Blueprint('main', __name__)

@main.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    result = predict(data['input'])
    return jsonify({"prediction": result.tolist()})
