import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import unittest
from src.util import get_ip_address, get_port, is_src, validate_ip, validate_port

class TestUtil(unittest.TestCase):

    # test valid conversion of a list of hex values to an ip address
    def test_get_ip_address_valid(self):
        self.assertEqual(get_ip_address(['c0', 'a8', '01', '01']), '192.168.1.1')

    # test when the hex list does not have the required 4 elements
    def test_get_ip_address_invalid_length(self):
        self.assertIsNone(get_ip_address(['c0', 'a8']))

    # test when the hex list contains an invalid hex value
    def test_get_ip_address_invalid_hex(self):
        self.assertIsNone(get_ip_address(['c0', 'a8', 'zz', '01']))

    # test valid conversion of two hex values to a port number
    def test_get_port_valid(self):
        self.assertEqual(get_port(['1f', '90']), '8080')

    # test when the hex list for the port has less than 2 elements
    def test_get_port_invalid_length(self):
        self.assertIsNone(get_port(['1f']))

    # test when the hex list for the port contains an invalid hex value
    def test_get_port_invalid_hex(self):
        self.assertIsNone(get_port(['1f', 'zz']))

    # test if two identical mac addresses match
    def test_is_src_match(self):
        self.assertTrue(is_src(['f8', '34', '41', '21', '87', '7a'], ['f8', '34', '41', '21', '87', '7a']))

    # test if two different mac addresses do not match
    def test_is_src_no_match(self):
        self.assertFalse(is_src(['f8', '34', '41', '21', '87', '7a'], ['00', '34', '41', '21', '87', '7a']))

    # test validation of a properly formatted and valid ip address
    def test_validate_ip_valid(self):
        self.assertTrue(validate_ip('192.168.1.1'))

    # test validation of an ip address with an octet out of range
    def test_validate_ip_invalid_format(self):
        self.assertFalse(validate_ip('192.168.1.256'))

    # test validation of an ip address with an invalid string format
    def test_validate_ip_invalid_string(self):
        self.assertFalse(validate_ip('abc.def.ghi.jkl'))

    # test validation of a valid port within the allowed range
    def test_validate_port_valid(self):
        self.assertTrue(validate_port('80'))

    # test validation of the lowest boundary value for a port (0)
    def test_validate_port_boundary_low(self):
        self.assertTrue(validate_port('0'))

    # test validation of the highest boundary value for a port (65535)
    def test_validate_port_boundary_high(self):
        self.assertTrue(validate_port('65535'))

    # test validation of a negative port, which is invalid
    def test_validate_port_invalid_negative(self):
        self.assertFalse(validate_port('-1'))

    # test validation of a port number exceeding the maximum allowed value (65535)
    def test_validate_port_invalid_above_range(self):
        self.assertFalse(validate_port('70000'))

    # test validation of a port number that is not numeric
    def test_validate_port_invalid_string(self):
        self.assertFalse(validate_port('port'))
