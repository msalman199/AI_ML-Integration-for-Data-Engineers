import json
import pandas as pd

class LogFeatureExtractor:
    """Extract features from log entries for ML model."""
    
    def __init__(self):
        self.severity_map = {'INFO': 0, 'WARNING': 1, 'ERROR': 2, 'CRITICAL': 3}
    
    def load_logs(self, log_file):
        """
        Load logs from JSON file.
        
        Args:
            log_file: Path to JSON log file
            
        Returns:
            List of log dictionaries
        """
        # TODO: Read and return JSON data from file
        pass
    
    def extract_features(self, logs):
        """
        Extract feature matrix and labels from logs.
        
        Args:
            logs: List of log dictionaries
            
        Returns:
            Tuple of (features_df, labels_series)
        """
        # TODO: Create lists to store features and labels
        
        # TODO: Iterate through logs and extract:
        # - severity (mapped to numeric)
        # - cpu_usage
        # - memory_usage
        # - error_count
        # - alert (label)
        
        # TODO: Create pandas DataFrame for features
        # TODO: Create pandas Series for labels
        
        # TODO: Return features and labels
        pass

if __name__ == "__main__":
    extractor = LogFeatureExtractor()
    logs = extractor.load_logs('training_logs.json')
    features, labels = extractor.extract_features(logs)
    print(f"Extracted {len(features)} samples with {len(features.columns)} features")
