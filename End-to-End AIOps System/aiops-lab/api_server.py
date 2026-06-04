from flask import Flask, jsonify, request
from db_manager import ClickHouseManager
import json

app = Flask(__name__)
db = ClickHouseManager()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "aiops-api"})

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """
    Get recent metrics with optional filtering.
    TODO: Query parameters: service, limit
    TODO: Return metrics from database
    """
    # TODO: Get query parameters
    # TODO: Query database with filters
    # TODO: Return JSON response
    pass

@app.route('/anomalies', methods=['GET'])
def get_anomalies():
    """
    Get detected anomalies.
    TODO: Query anomalies from last N hours
    """
    # TODO: Get hours parameter (default 24)
    # TODO: Query anomalies from database
    # TODO: Return JSON response
    pass

@app.route('/predict', methods=['POST'])
def predict_metrics():
    """
    Predict future metrics using AI model.
    TODO: Accept service name, return predictions
    """
    # TODO: Get service from request
    # TODO: Load historical data
    # TODO: Call predictor module
    # TODO: Return predictions
    pass

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
