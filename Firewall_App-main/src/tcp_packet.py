#tcp_packet.py

class TCPPacket:
    def __init__(self, MACaddress=None, srcIP=None, dstIP=None, srcPort=None, dstPort=None):
        """
        initialize a TCPPacket object.

        Parameters:
            MACaddress (str): MAC address of the packet.
            srcIP (str): source IP address.
            dstIP (str): destination IP address.
            srcPort (str): source port.
            dstPort (str): destination port.
        """
        self.MACaddress = MACaddress
        self.srcIP = srcIP
        self.dstIP = dstIP
        self.srcPort = srcPort
        self.dstPort = dstPort

    def getMACaddress(self):
        return self.MACaddress

    def getSrcIP(self):
        return self.srcIP

    def getDstIP(self):
        return self.dstIP

    def getSrcPort(self):
        return self.srcPort

    def getDstPort(self):
        return self.dstPort

    def __str__(self):
        return f"TCP packet: Src_ip:{self.srcIP} Dst_ip:{self.dstIP} Src_port:{self.srcPort} Dst_port:{self.dstPort}"


#example usage
if __name__ == "__main__":
    t = TCPPacket('f8:34:41:21:87:7a', '192.168.1.6', '192.168.1.1', '63439', '80')
    print(t)
    print("Source IP:", t.getSrcIP())
