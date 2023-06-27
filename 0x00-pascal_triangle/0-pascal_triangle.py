#!/usr/bin/env python3

"""This module simulates an interview question"""

def pascal_triangle(n):
    """Function returns a list of lists of
    integers representing the Pascal's triangle of n

    Args:
        n (int): The first and only parameter
    Returns:
        list: returns a list of lists
    """
    triangle = []
    if n <= 0:
        return triangle
