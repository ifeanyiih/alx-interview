#!/usr/bin/python3
"""Module contains a function
rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix"""
    new_row_size = len(matrix[0])
    new_matrix = []
    for _ in range(new_row_size):
        new_matrix.append([])

    current_index = 0
    for n_row in new_matrix:
        for row in matrix:
            n_row.insert(0, row[current_index])
        current_index += 1

    matrix.clear()
    for row in new_matrix:
        matrix.append(row)
