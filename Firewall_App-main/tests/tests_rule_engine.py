import unittest
from unittest.mock import patch, MagicMock
from src.rule_engine import RuleEngine, apply_rule

class TestRuleEngine(unittest.TestCase):

    # test if the rule engine loads inbound rules correctly
    @patch("configparser.ConfigParser.read", return_value=True)
    def test_load_inbound_rules(self, mock_read):
        rule_engine = RuleEngine()
        self.assertIsInstance(rule_engine, RuleEngine)

    # test when no inbound rules match the provided ip and port
    def test_check_inbound_rules_no_match(self):
        rule_engine = RuleEngine()
        result = rule_engine.check_inbound_rules('192.168.1.1', '80')
        self.assertEqual(result, "No rule associated! Please assign a rule.")

    # test if the rule engine handles a packet with missing fields
    def test_apply_rule_missing_fields(self):
        rule_engine = RuleEngine()
        packet = {'ip_address': None, 'port': None}
        result = apply_rule(rule_engine, packet)
        self.assertEqual(result, "Invalid packet!")

    # test if the rule engine applies an inbound rule correctly
    @patch("src.rule_engine.RuleEngine.check_inbound_rules", return_value="Accept")
    def test_apply_rule_inbound(self, mock_check_inbound):
        rule_engine = RuleEngine()
        packet = {'ip_address': '192.168.1.1', 'port': '80'}
        result = apply_rule(rule_engine, packet)
        self.assertEqual(result, "Accept")
