import json
import time
import random
from datetime import datetime
from pathlib import Path

class MetricsIngestion:
    """Simulates ingestion of operational metrics from various sources"""
    
    def __init__(self, output_dir='data'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def generate_metrics(self):
        """
        Generate simulated operational metrics.
        TODO: Implement metric generation with realistic patterns
        Returns: dict with timestamp, service, cpu, memory, latency, error_rate
        """
        # TODO: Create metric dictionary with current timestamp
        # TODO: Add service name (web, api, database, cache)
        # TODO: Add cpu_usage (0-100), memory_usage (0-100)
        # TODO: Add latency_ms (50-500), error_rate (0-10)
        pass
    
    def ingest_batch(self, batch_size=100):
        """
        Ingest a batch of metrics and save to file.
        TODO: Generate batch_size metrics and save as JSON lines
        """
        # TODO: Generate metrics batch
        # TODO: Write to file with timestamp in filename
        # TODO: Return filename
        pass

# Test ingestion
if __name__ == '__main__':
    ingestion = MetricsIngestion()
    # TODO: Ingest 3 batches of 100 metrics each
    print("Ingestion complete")
