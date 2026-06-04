import pandas as pd
import numpy as np
from statistical_detector import ZScoreDetector
from ml_detector import IsolationForestDetector
import pickle

def train_and_save_models(data_file: str):
    """
    Train both detectors and save to disk.
    
    Args:
        data_file: Path to training data CSV
    """
    # TODO: Load data
    # TODO: Extract feature values
    # TODO: Initialize both detectors
    # TODO: Train both models using fit()
    # TODO: Save models using pickle
    pass

if __name__ == "__main__":
    train_and_save_models('data.csv')
    print("Models trained and saved successfully")
