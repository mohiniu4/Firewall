import unittest
from unittest.mock import mock_open, patch
from src.helpers import load_packets

class TestHelpers(unittest.TestCase):

    # test loading packets from a valid file with correct data
    @patch("builtins.open", new_callable=mock_open, read_data="192.168.1.1,80\n192.168.1.2,443\n")
    def test_load_packets_valid(self, mock_file):
        packets = load_packets("test_packets.txt")
        self.assertEqual(len(packets), 2)  # expect two packets in the list
        self.assertEqual(packets[0], "192.168.1.1,80")  # check the first packet
        self.assertEqual(packets[1], "192.168.1.2,443")  # check the second packet

    # test loading packets from an empty file
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_packets_empty(self, mock_file):
        packets = load_packets("test_packets.txt")
        self.assertEqual(packets, [])  # expect an empty list for empty files

    # test handling of a file not found error
    @patch("builtins.open", side_effect=IOError("File not found"))
    def test_load_packets_file_not_found(self, mock_file):
        packets = load_packets("test_packets.txt")
        self.assertIsNone(packets)  # expect None when the file is not found
