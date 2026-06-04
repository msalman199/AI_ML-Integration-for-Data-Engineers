import numpy as np
import pandas as pd

def generate_normal_data(n_samples: int, seed: int = 42) -> np.ndarray:
    """
    Generate normal data points.
    
    Args:
        n_samples: Number of samples to generate
        seed: Random seed for reproducibility
    
    Returns:
        Array of normal data points
    """
    # TODO: Set random seed
    # TODO: Generate normal distribution data with mean=50, std=10
    pass

def inject_anomalies(data: np.ndarray, anomaly_ratio: float = 0.05) -> np.ndarray:
    """
    Inject anomalies into the dataset.
    
    Args:
        data: Original data array
        anomaly_ratio: Proportion of anomalies to inject
    
    Returns:
        Data array with injected anomalies
    """
    # TODO: Calculate number of anomalies
    # TODO: Select random indices for anomalies
    # TODO: Replace selected points with extreme values (mean ± 3*std)
    pass

def create_dataset(n_samples: int = 1000) -> pd.DataFrame:
    """
    Create complete dataset with features and labels.
    
    Args:
        n_samples: Total number of samples
    
    Returns:
        DataFrame with features and anomaly labels
    """
    # TODO: Generate normal data
    # TODO: Inject anomalies
    # TODO: Create labels (0=normal, 1=anomaly)
    # TODO: Create DataFrame with columns: 'value', 'timestamp', 'label'
    pass

if __name__ == "__main__":
    df = create_dataset(1000)
    df.to_csv('data.csv', index=False)
    print(f"Dataset created: {len(df)} samples")
    print(f"Anomalies: {df['label'].sum()}")
