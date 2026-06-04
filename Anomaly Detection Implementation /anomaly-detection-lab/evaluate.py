import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import pickle
from typing import Dict, Tuple

def load_model(model_path: str):
    """
    Load trained model from disk.
    
    Args:
        model_path: Path to pickled model
    
    Returns:
        Loaded model object
    """
    # TODO: Load and return model using pickle
    pass

def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """
    Calculate evaluation metrics.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
    
    Returns:
        Dictionary with precision, recall, f1-score
    """
    # TODO: Calculate precision
    # TODO: Calculate recall
    # TODO: Calculate F1-score
    # TODO: Return dictionary with all metrics
    pass

def evaluate_model(model, X: np.ndarray, y_true: np.ndarray, model_name: str) -> Dict:
    """
    Evaluate a single model.
    
    Args:
        model: Trained detector model
        X: Feature data
        y_true: True labels
        model_name: Name for reporting
    
    Returns:
        Dictionary with evaluation results
    """
    # TODO: Get predictions from model
    # TODO: Calculate metrics
    # TODO: Calculate confusion matrix
    # TODO: Return results dictionary
    pass

def compare_models(data_file: str):
    """
    Compare both models on test data.
    
    Args:
        data_file: Path to test data CSV
    """
    # TODO: Load test data
    # TODO: Load both models
    # TODO: Evaluate both models
    # TODO: Print comparison table
    pass

if __name__ == "__main__":
    compare_models('data.csv')
