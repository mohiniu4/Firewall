#util.py

import re

def get_ip_address(array):
    """
    convert a list of hexadecimal values to an IP address in dotted decimal format.

    parameters:
        array (list): list of hexadecimal string values representing an IP address.

    returns:
        str: IP address in dotted decimal format, or None if the input is invalid.
    """
    try:
        if len(array) != 4:
            raise ValueError("IP address must have exactly 4 octets.")
        return '.'.join(str(int(i, 16)) for i in array)
    except ValueError as e:
        print(f"Error in get_ip_address: {e}")
        return None

def get_port(hex_pair):
    """
    convert a hexadecimal pair to a decimal port number.

    parameters:
        hex_pair (list): a list of two hexadecimal string values representing a port.

    returns:
        str: Port number in decimal format, or None if the input is invalid.
    """
    try:
        if len(hex_pair) != 2:
            raise ValueError("Port must be represented by exactly two hexadecimal values.")
        hex_string = hex_pair[0] + hex_pair[1]
        return str(int(hex_string, 16))
    except ValueError as e:
        print(f"Error in get_port: {e}")
        return None

def is_src(my_address, address):
    """
    check if a given address matches the specified MAC address.

    parameters:
        my_address (list): List representing the device's MAC address.
        address (list): List representing the source MAC address in the packet.

    returns:
        bool: True if the addresses match, otherwise False.
    """
    return my_address == address

def validate_ip(ip_address):
    """
    validate if the given IP address is in the correct dotted decimal format.

    parameters:
        ip_address (str): the IP address to validate.

    returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip_address):
        return all(0 <= int(octet) <= 255 for octet in ip_address.split('.'))
    return False

def validate_port(port):
    """
    validate if the given port number is within the valid range (0-65535).

    parameters:
        port (str): the port number to validate.

    returns:
        bool: True if valid, False otherwise.
    """
    try:
        port_num = int(port)
        return 0 <= port_num <= 65535
    except ValueError:
        return False

#example usage
if __name__ == "__main__":
    print(is_src(['f8', '34', '41', '21', '87', '7a'], ['f8', '34', '41', '21', '87', '7a']))  #true
    print(is_src(['f8', '34', '41', '21', '87', '7a'], ['f8', '34', '41', '21', '87', '7']))    #false
    print(get_ip_address(['c0', 'a8', '01', '01']))  #192.168.1.1
    print(get_ip_address(['c0', 'a8']))  #error, none
    print(get_port(['1f', '90']))  #8080
    print(get_port(['1f']))  #error, none
    print(validate_ip('192.168.1.1'))  #true
    print(validate_ip('256.256.256.256'))  #false
    print(validate_port('80'))  #true
    print(validate_port('70000'))  #false
