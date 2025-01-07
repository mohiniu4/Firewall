#core.py

from helpers import load_packets
from rule_engine import RuleEngine, apply_rule
from tcp_packet import TCPPacket
from udp_packet import UDPPacket
from util import get_ip_address, get_port

def process_packets(packets, packet_type, rule_engine):
    """
    process packets of a specific type (TCP or UDP), applying rules.
    
    parameters:
        packets (list): list of raw packet data.
        packet_type (str): either "TCP" or "UDP".
        rule_engine (RuleEngine): instance of the RuleEngine.

    returns:
        none
    """
    print(f"\nProcessing {packet_type} Packets:")
    for line in packets:
        #assume test packet format is "srcIP,dstPort"
        try:
            srcIP, dstPort = line.split(",")
            MACaddress = None  #placeholder since MAC is not in test data
            dstIP = None       #placeholder since dstIP is not in test data
            srcPort = None     #placeholder since srcPort is not in test data

            #create packet object
            packet = (TCPPacket(MACaddress, srcIP, dstIP, srcPort, dstPort)
                      if packet_type == 'TCP'
                      else UDPPacket(MACaddress, srcIP, dstIP, srcPort, dstPort))
            print(packet)

            #apply rules to the packet
            result = apply_rule(rule_engine, {'ip_address': srcIP, 'port': dstPort})
            print(f"Action: {result}")
        except ValueError:
            print(f"Error processing line: {line}. Ensure it follows 'srcIP,dstPort' format.")

def main():
    """
    main function to load, process, and apply rules to TCP and UDP packets.
    """
    #load packet data
    tcp_packets = load_packets('packets/test_tcp_packets.txt')
    udp_packets = load_packets('packets/test_udp_packets.txt')

    if not tcp_packets or not udp_packets:
        print("Failed to load packet data. Exiting.")
        return

    #initialize Rule Engine
    rule_engine = RuleEngine()

    #process and apply rules to TCP packets
    process_packets(tcp_packets, 'TCP', rule_engine)

    #process and apply rules to UDP packets
    process_packets(udp_packets, 'UDP', rule_engine)

if __name__ == "__main__":
    main()
