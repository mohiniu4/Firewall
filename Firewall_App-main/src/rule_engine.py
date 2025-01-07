#rule_engine.py

import configparser
import logging

#configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RuleEngine:
    def __init__(self, inbound_rules_file='src/inbound rules.ini', outbound_rules_file='src/outbound rules.ini'):
        self.in_config = configparser.ConfigParser()
        self.out_config = configparser.ConfigParser()
        
        #load inbound and outbound rules from configuration files
        self._load_rules(self.in_config, inbound_rules_file, "Inbound")
        self._load_rules(self.out_config, outbound_rules_file, "Outbound")

    def _load_rules(self, config, file_path, rule_type):
        """load rules from a file and handle errors if the file is missing or unreadable."""
        try:
            config.read(file_path)
            logging.info(f"{rule_type} rules loaded successfully from {file_path}.")
        except Exception as e:
            logging.error(f"Failed to load {rule_type} rules from {file_path}: {e}")
            raise

    def check_inbound_rules(self, ip_address, port):
        """check if a packet meets inbound rules for a given IP address and port."""
        return self._check_rules(self.in_config, ip_address, port)

    def check_outbound_rules(self, ip_address, port):
        """check if a packet meets outbound rules for a given IP address and port."""
        return self._check_rules(self.out_config, ip_address, port)

    def _check_rules(self, config, ip_address, port):
        """helper function to evaluate rules in a given configuration."""
        for section, action in [('Accepting ip', 'Accept'), ('Declining ip', 'Decline'), ('Rejecting ip', 'Reject')]:
            if self._is_rule_match(config, section, ip_address, port):
                return action
        return "No rule associated! Please assign a rule."

    def _is_rule_match(self, config, section, ip_address, port):
        """
        check if a given IP address and port match any rules in the specified section.
        
        parameters:
            config (ConfigParser): the configuration object.
            section (str): the section of the rules ('Accepting ip', 'Declining ip', 'Rejecting ip').
            ip_address (str): the IP address to check.
            port (str): the port to check.

        returns:
            bool: True if there is a match, otherwise False.
        """
        if section in config:
            for ip, ports in config[section].items():
                if ip == ip_address and port in ports.split(","):
                    logging.info(f"Match found in section '{section}': IP={ip_address}, Port={port}")
                    return True
        return False


def apply_rule(rule_engine, packet):
    """
    apply rules to a packet using the RuleEngine.

    parameters:
        rule_engine (RuleEngine): an instance of the RuleEngine class.
        packet (dict): a dictionary containing packet information, including 'ip_address' and 'port'.

    returns:
        str: the result of applying the rules ('Accept', 'Decline', 'Reject', or 'No rule associated!').
    """
    ip_address = packet.get('ip_address')
    port = packet.get('port')

    if not ip_address or not port:
        logging.warning("Invalid packet: Missing 'ip_address' or 'port'.")
        return "Invalid packet!"

    #check inbound rules
    inbound_result = rule_engine.check_inbound_rules(ip_address, port)
    if inbound_result != "No rule associated! Please assign a rule.":
        return inbound_result

    #check outbound rules
    return rule_engine.check_outbound_rules(ip_address, port)


#example usage
if __name__ == "__main__":
    rule_engine = RuleEngine()
    test_packet = {'ip_address': '192.168.1.6', 'port': '63449'}
    result = apply_rule(rule_engine, test_packet)
    logging.info(f"Result for packet: {result}")
