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
    shift = 7
    binary_data = []
    any_ = []
    for n in data:
        shift = 7
        bin_ = ""
        while shift >= 0:
            if n & (1 << shift):
                digit = 1
            else:
                digit = 0
            bin_ += str(digit)
            shift -= 1
        binary_data.append(bin_)


    n = 0
    while n < len(binary_data):
        if binary_data[n].startswith('0'):
            any_.append(0)
        elif binary_data[n].startswith('110'):
            if (n + 1) < len(binary_data) \
                    and binary_data[n + 1].startswith('10'):
                any_.append(0)
                n = n + 2
                continue
            else:
                any_.append(1)
        elif binary_data[n].startswith('1110'):
            if (n + 2) < len(binary_data) \
                and binary_data[n + 1].startswith('10') and \
                    binary_data[n + 2].startswith('10'):
                any_.append(0)
                n = n + 3
                continue
            else:
                any_.append(1)
        elif binary_data[n].startswith('11110'):
            if (n + 3) < len(binary_data) \
                and binary_data[n + 1].startswith('10') and \
                binary_data[n + 2].startswith('10') and \
                    binary_data[n + 3].startswith('10'):
                any_.append(0)
                n = n + 4
                continue
            else:
                any_.append(1)
        else:
            any_.append(1)
        n = n + 1

    if any(any_):
        return False
    return True
