Firewall Application

Overview:
The Firewall Application is a Python-based tool for simulating firewall functionality. It allows users to filter and process TCP/UDP packets based on predefined inbound and outbound rules. The project uses configuration files to define rules and logs all actions for traceability.



Features:
Rule-based filtering of network packets.
Supports both TCP and UDP protocols.
Configurable inbound and outbound rules via .ini files.
Robust error handling for malformed packets and invalid configurations.
Unit-tested for reliability with extensive test coverage.
Logging for debugging and traceability.



Project Structure:
src/: Contains the source code for the project.
core.py: Main logic for processing packets and applying rules.
rule_engine.py: Handles rule definitions and their application.
tcp_packet.py: Defines the TCP packet class.
udp_packet.py: Defines the UDP packet class.
helpers.py: Contains utility functions for loading packets.
util.py: Includes validation and data conversion utilities.
packets/: Contains sample packet data files.
test_packets.txt, test_tcp_packets.txt, test_udp_packets.txt: Simulated packet data for testing.
tests/: Contains unit tests for the project.
tests_helpers.py, tests_rule_engine.py, etc.
install_firewall.py: Automates environment setup and dependency installation.
firewall_app.py: Entry point for running the firewall application.
requirements.txt: Specifies project dependencies.



Prerequisites:
Python Version:
Python 3.7 or higher is recommended.
Dependencies:
Install required Python packages by running:
pip install -r requirements.txt

Current dependencies:
configparser: For parsing rule files.
Setup Instructions
Clone the repository:
git clone https://github.com/mardini2/Firewall_App
cd <repository-folder>

Install dependencies:
python install_firewall.py

Verify configuration files:
Make sure the following files exist in the src/ folder:
firewall_rules.ini
inbound rules.ini
outbound rules.ini
If missing, create or configure them with appropriate rules.



How It Works:

Rules:
Define inbound and outbound rules in .ini files. Example:
[Accepting ip]
192.168.1.1 = 80,443
[Rejecting ip]
10.0.0.1 = 22
src_ip and src_port are matched for filtering.

Packets:
Packet data is loaded from .txt files in the packets/ folder.
Packet format: <src_ip>,<dst_port>. Example:
192.168.1.1,80

Rule Application:
The RuleEngine class evaluates each packet against the rules.
Outcomes: Accept, Decline, Reject, or No rule associated.

Output:
Logs actions for each packet, including rule matches and errors.
Running the Application

Execute the main application:
python firewall_app.py



To test the application:
Run unit tests:
python -m unittest discover -s tests

Example output:
Packet: {'ip_address': '192.168.1.1', 'port': '80'} -> Result: Accept
Modify packets/ files or .ini rules to customize behavior.



Extending the Project:
Add Support for IPv6:
Extend the validate_ip function in util.py to handle IPv6.

Additional Protocols:
Create new packet classes for protocols like ICMP or DNS.

Performance Testing:
Use tools like timeit to benchmark processing speed with large packet files.



Troubleshooting:
Missing Dependencies:
Reinstall dependencies using:
pip install -r requirements.txt

Malformed Packets:
Ensure packet files follow the src_ip,dst_port format.
Rule Not Applied:
Check if the .ini file contains a matching rule for the packet.



Contributing:
Fork the repository and create a feature branch.
Ensure all new features are unit tested.
Open a pull request with a detailed description of the changes.
