#!/usr/bin/python3

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
    lastIndex = -1
    if n <= 0:
        return triangle

    for i in range(1, n + 1):
        if lastIndex == -1:
            row = [1]
            lastIndex = 0
            triangle.append(row)
        else:
            row = [1]
            last = triangle[lastIndex]

            for i in range(len(last)):
                if i + 1 < len(last):
                    sum = last[i] + last[i + 1]
                    row.append(sum)
                else:
                    row.append(last[i])
            triangle.append(row)
            lastIndex = lastIndex + 1
    return triangle
