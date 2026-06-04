import random
import json
from datetime import datetime, timedelta

def generate_log_entry(timestamp, severity, cpu_usage, memory_usage, error_count, alert):
    """
    Generate a single log entry with system metrics.
    
    Args:
        timestamp: Log timestamp
        severity: Log severity level
        cpu_usage: CPU usage percentage
        memory_usage: Memory usage percentage
        error_count: Number of errors in time window
        alert: Boolean indicating if alert should trigger
    
    Returns:
        Dictionary containing log entry
    """
    # TODO: Create and return a dictionary with all parameters
    pass

def generate_training_data(num_samples=1000, output_file='training_logs.json'):
    """
    Generate synthetic training data with normal and alert conditions.
    
    Args:
        num_samples: Number of log entries to generate
        output_file: Output JSON file path
    """
    logs = []
    start_time = datetime.now() - timedelta(days=7)
    
    for i in range(num_samples):
        timestamp = start_time + timedelta(minutes=i)
        
        # TODO: Implement logic to create alert conditions
        # Alert conditions: high CPU (>85%) OR high memory (>90%) OR errors (>5)
        # Normal conditions: moderate resource usage, few errors
        
        # TODO: Randomly decide if this should be an alert scenario (30% probability)
        
        # TODO: Generate appropriate metrics based on alert/normal condition
        
        # TODO: Create log entry and append to logs list
        
        pass
    
    # TODO: Write logs to JSON file
    pass

if __name__ == "__main__":
    generate_training_data()
    print("Training data generated: training_logs.json")
