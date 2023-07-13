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
    if type(n) not in [int]:
        return 0
    if not math.isfinite(n):
        return 0
    if n <= 0:
        return 0
    if n == 1:
        return 1
    c = 'H'
    copyAll = 1
    paste = 1
    s = 'HH'
    while len(s) != n:
        if n % len(s) == 0:
            copyAll += 1
            paste += 1
            c = s
            s = s + c
        else:
            s = s + c
            paste += 1
    return (copyAll + paste)
