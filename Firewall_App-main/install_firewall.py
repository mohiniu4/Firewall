#install_firewall.py

import os
import subprocess
import logging

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def install_dependencies():
    """
    installs necessary Python dependencies for the firewall application.
    """
    logging.info("Installing required Python packages...")
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        logging.info("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install dependencies: {e}")
        raise

def setup_config():
    """
    makes sure the necessary configuration files are in place.
    """
    logging.info("Setting up configuration files...")
    
    #example check for configuration files
    required_files = ["src/firewall_rules.ini", "src/inbound rules.ini", "src/outbound rules.ini"]
    for file in required_files:
        if not os.path.exists(file):
            logging.error(f"Configuration file {file} is missing.")
            raise FileNotFoundError(f"Configuration file {file} is missing.")
    
    logging.info("Configuration files are set up correctly.")

def initialize_environment():
    """
    performs any environment-specific setup.
    """
    logging.info("Initializing environment...")
    try:
        #example: creating necessary directories
        os.makedirs("packets", exist_ok=True)
        os.makedirs("images", exist_ok=True)
        logging.info("Environment initialized successfully.")
    except Exception as e:
        logging.error(f"Failed to initialize environment: {e}")
        raise

def main():
    """
    main function to set up the firewall system.
    """
    logging.info("Starting firewall installation process...")
    install_dependencies()
    setup_config()
    initialize_environment()
    logging.info("Firewall installation completed successfully.")

if __name__ == "__main__":
    main()
