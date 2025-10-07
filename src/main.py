"""
Main entry point for PDF Type Classification project.
Initializes and runs the pipeline.
"""

from src.pipeline import run_pipeline

def main():
    print("Starting PDF Type Classification pipeline...")
    run_pipeline()
    print("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()
