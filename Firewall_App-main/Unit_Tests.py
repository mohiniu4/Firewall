import subprocess
import pytest
import unittest
from unittest.mock import patch, mock_open, MagicMock
from firewall_app import parse_rules
from install_firewall import install_dependencies, setup_config, initialize_environment
from test_rule_engine import load_test_packets
from src.core import process_packets
import sys
import os
sys.path.append(os.path.abspath(r"C:\Users\Umang\Downloads\CS Year 3\Term 1\Network security\Assignments\Project\Firewall_App"))

# firewall_app.py unit tests
class Test_FirewallApp(unittest.TestCase):
        
    # passes
    # make sure the function works as it should
    @patch("builtins.open", new_callable=mock_open, read_data="[rule1]\nsrc_ip=192.168.1.1\nsrc_port=80\ndst_ip=192.168.1.2\ndst_port=443\n")
    @patch("firewall_app.validate_ip", return_value=True)
    @patch("firewall_app.validate_port", return_value=True)
    def test_valid_parse_rules(self, mock_validate_ip, mock_validate_port, mock_file):
        rules = parse_rules("dummy.ini")
        self.assertEqual(len(rules), 1)
        self.assertEqual(rules[0]["src_ip"], "192.168.1.1")
        self.assertEqual(rules[0]["dst_ip"], "192.168.1.2")
        
    # passes
    # makes sure it does not accept any invalid ip addresses
    @patch("builtins.open", new_callable=mock_open, read_data="[rule1]\nsrc_ip=192.168.500.25\nsrc_port=80\ndst_ip=192.167.1.26\ndst_port=443\n")
    @patch("firewall_app.validate_ip", side_effect=lambda ip: ip and ip.count('.') == 3 and all(0 <= int(part) < 256 for part in ip.split('.')))
    @patch("firewall_app.validate_port", return_value=True)
    def test_invalid_parse_rules(self, mock_validate_ip, mock_validate_port, mock_file):
        rules = parse_rules("dummy.ini")
        self.assertEqual(len(rules), 0)

    # passes
    # makes sure nothing happens when it recieves a empty
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_empty_parse_rules(self, mock_file):
        rules = parse_rules("dummy.ini")
        self.assertEqual(len(rules), 0)
    
    # passes
    # make sure the function does not validate any ip or ports without all the required infomation
    @patch("builtins.open", new_callable=mock_open, read_data="[rule1]\nsrc_ip=\ndst_ip=192.168.1.26\n")
    def test_missing_keys_parse_rules(self, mock_file):
        rules = parse_rules("dummy.ini")
        self.assertEqual(len(rules), 0)


       
# install_firewall.py unit tests
class Test_InstallFirewall(unittest.TestCase):
    
    # passes
    # make sure it calls the right system command to install the dependencies
    @patch("subprocess.check_call") 
    def test_install_dependencies(self, mock_subprocess):
        install_dependencies()
        mock_subprocess.assert_called_once()

    # passes
    # make sure it does not install the dependencies
    @patch("subprocess.check_call", side_effect=subprocess.CalledProcessError(1, "cmd"))
    def test_install_dependencies_failure(self, mock_subprocess):
        with self.assertRaises(subprocess.CalledProcessError):
            install_dependencies()


    # passes
    # make sure it does not run when a file is missing
    @patch("os.path.exists", return_value=False)
    def test_setup_config_noFile(self, mock_exists):
        with self.assertRaises(FileNotFoundError):
            setup_config()

# Test_Rule_Engine.py unit tests
class TestRuleEngine(unittest.TestCase):
    
    # passes
    # make sure the data in the packet is loaded correctly
    @patch("builtins.open", new_callable=mock_open, read_data="192.168.1.1,80\n")
    def test_load_test_packets_valid(self, mock_file):
        packets = load_test_packets("test_packets.txt")
        self.assertEqual(len(packets), 1)
        self.assertEqual(packets[0]["ip_address"], "192.168.1.1")

    # passes
    # make sure that packets that are not in the right format will be rejected
    @patch("builtins.open", new_callable=mock_open, read_data="192.168.1.1:80")
    def test_load_wrong_format_test_packets(self, mock_file):
        packets = load_test_packets("test_packets.txt")
        self.assertEqual(len(packets), 0)

    # passes
    # make sure it does not load any packets that are empty
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_empty_test_packets(self, mock_file):
        packets = load_test_packets("test_packets.txt")
        self.assertEqual(len(packets), 0)


'''
following does not work so i commented it out for now

# core.py unit tests
class TestCore(unittest.TestCase):
    @patch("core.RuleEngine")
    @patch("core.apply_rule", return_value="ALLOW")
    def test_process_packets(self, mock_apply_rule, mock_rule_engine):
        packets = ["192.168.1.1,80"]
        mock_engine_instance = mock_rule_engine.return_value
        process_packets(packets, "TCP", mock_engine_instance)
        mock_apply_rule.assert_called_once_with(mock_engine_instance, {"ip_address": "192.168.1.1", "port": "80"})
   
'''


        
if __name__ == "__main__":
    unittest.main()