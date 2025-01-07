#test_rule_engine

from src.rule_engine import RuleEngine, apply_rule

def load_test_packets(file_path):
    """
    load test packets from a file.

    parameters:
        file_path (str): path to the file containing test packets.

    returns:
        list: a list of dictionaries, where each dictionary represents a packet with 'ip_address' and 'port'.
    """
    packets = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                ip, port = line.strip().split(',')
                packets.append({'ip_address': ip, 'port': port})
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except ValueError:
        print(f"Error: Malformed line in {file_path}. Ensure each line is formatted as 'ip_address,port'.")
    return packets

def test_rule_engine():
    """
    test the RuleEngine by applying rules to a set of test packets.
    """
    print("Initializing RuleEngine...")
    rule_engine = RuleEngine()

    print("Loading test packets...")
    test_packets = load_test_packets('packets/test_packets.txt')

    if not test_packets:
        print("No test packets loaded. Exiting.")
        return

    print("Testing packets against rules...")
    for packet in test_packets:
        result = apply_rule(rule_engine, packet)
        print(f"Packet: {packet} -> Result: {result}")

if __name__ == "__main__":
    test_rule_engine()
