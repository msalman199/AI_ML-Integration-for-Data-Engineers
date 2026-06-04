import requests
import json

def test_health():
    """Test health check endpoint."""
    # TODO: Send GET request to /health
    # TODO: Print response
    pass

def test_prediction(features):
    """
    Test prediction endpoint.
    
    Args:
        features: List of feature values
    """
    # TODO: Send POST request to /predict with features
    # TODO: Print prediction results
    pass

if __name__ == "__main__":
    base_url = "http://localhost:5000"
    
    # TODO: Test health endpoint
    
    # TODO: Test prediction with sample data
    # Example: [35, 12, 65.5, 786.0] (age, tenure, monthly_charges, total_charges)
    
    pass
