#!/usr/bin/env python3
import sys
import time
from multiprocessing import Process
from ingestion import MetricsIngestion
from spark_processor import SparkProcessor
from db_manager import ClickHouseManager
from api_server import app
from workflow import AIOpsWorkflow
from monitor import SystemMonitor

def setup_system():
    """Initialize system components"""
    print("Setting up AIOps system...")
    
    # Initialize database
    db = ClickHouseManager()
    db.create_tables()
    print("Database initialized")
    
    # Generate initial data
    ingestion = MetricsIngestion()
    for i in range(3):
        ingestion.ingest_batch(100)
    print("Initial data generated")
    
    # Process initial data
    processor = SparkProcessor()
    # TODO: Process initial data batch
    print("Initial processing complete")

def run_api_server():
    """Run API server in separate process"""
    app.run(host='0.0.0.0', port=5000, debug=False)

def run_workflow():
    """Run workflow automation"""
    workflow = AIOpsWorkflow()
    workflow.start()

def run_monitor():
    """Run system monitor"""
    monitor = SystemMonitor()
    monitor.monitor_loop()

if __name__ == '__main__':
    # Setup system
    setup_system()
    
    # Start components in separate processes
    api_process = Process(target=run_api_server)
    workflow_process = Process(target=run_workflow)
    monitor_process = Process(target=run_monitor)
    
    api_process.start()
    print("API server started on port 5000")
    
    workflow_process.start()
    print("Workflow automation started")
    
    monitor_process.start()
    print("System monitor started")
    
    print("\nAIOps system is running!")
    print("API available at: http://localhost:5000")
    print("Press Ctrl+C to stop")
    
    try:
        api_process.join()
    except KeyboardInterrupt:
        print("\nShutting down...")
        api_process.terminate()
        workflow_process.terminate()
        monitor_process.terminate()
