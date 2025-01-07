import unittest
from src.udp_packet import UDPPacket
from src.tcp_packet import TCPPacket

class TestUDPPacket(unittest.TestCase):

    # test the creation of a udp packet and verify all attributes are set correctly
    def test_udp_packet_creation(self):
        packet = UDPPacket('00:11:22:33:44:55', '192.168.1.1', '192.168.1.2', '1234', '80')
        self.assertEqual(packet.getMACaddress(), '00:11:22:33:44:55')
        self.assertEqual(packet.getSrcIP(), '192.168.1.1')
        self.assertEqual(packet.getDstIP(), '192.168.1.2')
        self.assertEqual(packet.getSrcPort(), '1234')
        self.assertEqual(packet.getDstPort(), '80')

    # test the string representation of a udp packet
    def test_udp_packet_to_string(self):
        packet = UDPPacket(None, '192.168.1.1', '192.168.1.2', '1234', '80')
        self.assertEqual(str(packet), 'UDP packet: Src_ip:192.168.1.1 Dst_ip:192.168.1.2 Src_port:1234 Dst_port:80')


class TestTCPPacket(unittest.TestCase):

    # test the creation of a tcp packet and verify all attributes are set correctly
    def test_tcp_packet_creation(self):
        packet = TCPPacket('00:11:22:33:44:55', '192.168.1.1', '192.168.1.2', '1234', '80')
        self.assertEqual(packet.getMACaddress(), '00:11:22:33:44:55')
        self.assertEqual(packet.getSrcIP(), '192.168.1.1')
        self.assertEqual(packet.getDstIP(), '192.168.1.2')
        self.assertEqual(packet.getSrcPort(), '1234')
        self.assertEqual(packet.getDstPort(), '80')

    # test the string representation of a tcp packet
    def test_tcp_packet_to_string(self):
        packet = TCPPacket(None, '192.168.1.1', '192.168.1.2', '1234', '80')
        self.assertEqual(str(packet), 'TCP packet: Src_ip:192.168.1.1 Dst_ip:192.168.1.2 Src_port:1234 Dst_port:80')
