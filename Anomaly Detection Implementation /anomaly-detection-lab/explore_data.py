import pandas as pd
import matplotlib.pyplot as plt

def load_and_describe(filepath: str) -> pd.DataFrame:
    """
    Load dataset and print basic statistics.
    
    Args:
        filepath: Path to CSV file
    
    Returns:
        Loaded DataFrame
    """
    # TODO: Load CSV file
    # TODO: Print shape, head, and describe()
    pass

def visualize_data(df: pd.DataFrame, output_file: str = 'data_distribution.png'):
    """
    Create visualization of data distribution.
    
    Args:
        df: DataFrame with data
        output_file: Path to save plot
    """
    # TODO: Create histogram of values
    # TODO: Mark anomalies in different color
    # TODO: Save figure
    pass

if __name__ == "__main__":
    df = load_and_describe('data.csv')
    visualize_data(df)
