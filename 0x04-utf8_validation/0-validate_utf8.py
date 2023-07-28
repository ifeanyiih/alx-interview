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


def parseBin(n):
    """parse a given integer to binary"""
    bin_str = ""
    num = n
    while num > 0:
        bin_str = str(num % 2) + bin_str
        num //= 2
    if len(bin_str) < 8:
        bin_str = '0' + bin_str
    if len(bin_str) > 8:
        bin_str = bin_str[len(bin_str) - 8:]
    return bin_str


def validUTF8(data):
    """Validates UTF-8 data
    Args:
        data (list): a list of ints
    Returns:
        bool: True if valid, else False
    """
    toVal = map(lambda n: n & 128, data)
    bins = list(map(parseBin, data))
    any_ = []
    for n in range(len(bins)):
        if bins[n].startswith('0'):
            any_.append(0)
        elif bins[n].startswith('110'):
            if bins[n + 1].startswith('10'):
                any_.append(0)
                n += 2
            else:
                any_.append(1)
                break
        elif bins[n].startswith('1110'):
            if bins[n + 1].startswith('10') and bins[n + 2].startswith('10'):
                any_.append(0)
                n += 3
                continue
            else:
                any_.append(1)
                break
        elif bins[n].startswith('11110'):
            if bins[n + 1].startswith('10') and \
                bins[n + 2].startswith('10') and \
                    bins[n + 3].startswith('10'):
                any_.append(0)
                n += 4
                continue
            else:
                any_.append(1)
                break

    if any(any_):
        return False
    return True
