#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to
handle the 8 least significant bits of each integer

For 1 byte UTF-8 characters, the most significant bit is 0
"""


def validUTF8(data):
    """Validates UTF-8 data
    Args:
        data (list): a list of ints
    Returns:
        bool: True if valid, else False
    """
    toVal = map(lambda n: n & 128, data)
    if any(toVal):
        return False
    return True
