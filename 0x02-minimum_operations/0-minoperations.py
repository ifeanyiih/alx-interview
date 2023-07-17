#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
"""
import math


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations
    needed to result in exactly n H characters"""
    ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            ops += min_ops
            n /= min_ops
        min_ops += 1
    return ops
