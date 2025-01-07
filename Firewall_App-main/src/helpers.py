#helpers.py

import logging

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_packets(file_path):
    """
    load packet data from a given file.

    parameters:
        file_path (str): the path to the file containing packet data.

    returns:
        list: a list of packet strings, or None if the file cannot be read.
    """
    try:
        logging.info(f"Loading packets from {file_path}...")
        with open(file_path, 'r') as file:
            packets = [line.strip() for line in file if line.strip()]
            if not packets:
                logging.warning(f"No packets found in {file_path}.")
            return packets
    except IOError as e:
        logging.error(f"Error: Could not open file {file_path}: {e}")
        return None
