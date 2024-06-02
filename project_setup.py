import os
import subprocess

def install_requirements():
    """Install the required packages."""
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

def create_artifacts():
    """Run the necessary scripts to create initial artifacts."""
    # Call the train_pipeline script to perform the training and artifact creation
    subprocess.check_call(["python", "src/pipeline/train_pipeline.py"])

def main():
    install_requirements()
    create_artifacts()

if __name__ == "__main__":
    main()



