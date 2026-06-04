from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Global model variable
model = None

def load_model():
    """
    Load the latest trained model.
    
    Returns:
        Loaded model object
    """
    # TODO: Load model from models/latest_model.pkl
    # TODO: Handle case where model doesn't exist
    pass

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    # TODO: Return JSON with status and model loaded state
    pass

@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint.
    
    Expected JSON format:
    {
        "features": [value1, value2, value3, value4]
    }
    
    Returns:
        JSON with prediction and probability
    """
    # TODO: Extract features from request JSON
    # TODO: Validate input
    # TODO: Make prediction using loaded model
    # TODO: Return prediction and probability as JSON
    pass

@app.route('/reload', methods=['POST'])
def reload_model():
    """Reload the model (useful after retraining)."""
    # TODO: Reload the model
    # TODO: Return success/failure status
    pass

if __name__ == '__main__':
    # TODO: Load model on startup
    # TODO: Run Flask app on port 5000
    pass
