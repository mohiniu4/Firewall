#firewall_app.py

import logging
import configparser
from src.util import validate_ip, validate_port
from src.rule_engine import RuleEngine, apply_rule
from src.helpers import load_packets

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_rules(filename="src/firewall_rules.ini"):
    """Parse firewall rules from an .ini file and validate IP and port values."""
    config = configparser.ConfigParser()
    config.read(filename)
    
    rules = []
    for section in config.sections():
        rule = {
            'direction': section,
            'protocol': config[section].get('protocol'),
            'src_ip': config[section].get('src_ip'),
            'src_port': config[section].get('src_port'),
            'dst_ip': config[section].get('dst_ip'),
            'dst_port': config[section].get('dst_port'),
            'action': config[section].get('action')
        }

        #check for missing or invalid fields
        if not rule['src_ip'] or not rule['dst_ip']:
            logging.warning(f"Missing IP in rule: {rule}")
            continue
        if not rule['src_port'] or not rule['dst_port']:
            logging.warning(f"Missing port in rule: {rule}")
            continue

        #validate IPs and ports
        if validate_ip(rule['src_ip']) and validate_ip(rule['dst_ip']):
            if validate_port(rule['src_port']) and validate_port(rule['dst_port']):
                rules.append(rule)
            else:
                logging.warning(f"Invalid port in rule: {rule}")
        else:
            logging.warning(f"Invalid IP in rule: {rule}")
    
    return rules

def main():
    #initialize rule engine
    rule_engine = RuleEngine()
    
    #load TCP and UDP packet data
    tcp_packets = load_packets('packets/tcp.txt')
    udp_packets = load_packets('packets/udp.txt')

    if not tcp_packets or not udp_packets:
        logging.error("Failed to load packets. Exiting.")
        return

    #parse rules from the firewall_rules.ini file
    rules = parse_rules()
    if not rules:
        logging.error("No valid rules found in firewall_rules.ini. Exiting.")
        return
    
    logging.info("Applying firewall rules to packets...")

    for packet in tcp_packets:
        logging.info(f"Processing TCP Packet: {packet.strip()}")
        #logic to apply rules to TCP packets

    for packet in udp_packets:
        logging.info(f"Processing UDP Packet: {packet.strip()}")
        #logic to apply rules to UDP packets

    logging.info("Finished applying rules.")

if __name__ == '__main__':
    main()
