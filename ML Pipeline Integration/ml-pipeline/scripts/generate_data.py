import pandas as pd
import numpy as np
from datetime import datetime

def generate_sample_data(n_samples=1000):
    """
    Generate synthetic customer data for churn prediction.
    
    Args:
        n_samples: Number of samples to generate
    
    Returns:
        DataFrame with features and target
    """
    np.random.seed(42)
    
    # TODO: Generate features (age, tenure, monthly_charges, total_charges)
    # TODO: Create target variable (churn: 0 or 1)
    # TODO: Return as pandas DataFrame
    
    pass

def save_data(df, filepath):
    """Save DataFrame to CSV with timestamp."""
    # TODO: Implement data saving with timestamp in filename
    pass

if __name__ == "__main__":
    # TODO: Generate data and save to data directory
    pass
