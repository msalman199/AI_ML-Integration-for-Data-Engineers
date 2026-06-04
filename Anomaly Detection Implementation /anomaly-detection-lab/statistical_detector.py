import numpy as np
import pandas as pd
from typing import Tuple

class ZScoreDetector:
    """Detect anomalies using Z-score method."""
    
    def __init__(self, threshold: float = 3.0):
        """
        Initialize detector.
        
        Args:
            threshold: Z-score threshold for anomaly detection
        """
        self.threshold = threshold
        self.mean = None
        self.std = None
    
    def fit(self, X: np.ndarray) -> 'ZScoreDetector':
        """
        Calculate mean and standard deviation from training data.
        
        Args:
            X: Training data array
        
        Returns:
            Self for method chaining
        """
        # TODO: Calculate and store mean
        # TODO: Calculate and store standard deviation
        pass
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict anomalies based on Z-score.
        
        Args:
            X: Data to evaluate
        
        Returns:
            Binary array (1=anomaly, 0=normal)
        """
        # TODO: Calculate Z-scores
        # TODO: Return binary predictions based on threshold
        pass
    
    def score(self, X: np.ndarray) -> np.ndarray:
        """
        Return anomaly scores (absolute Z-scores).
        
        Args:
            X: Data to score
        
        Returns:
            Array of anomaly scores
        """
        # TODO: Calculate and return absolute Z-scores
        pass
