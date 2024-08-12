#!/usr/bin/python3
"""
Module that rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
   To rotate a n x n 2D matrix 90 degrees clockwise in place.

    Parameters:
    matrix: The n x n matrix to be rotated.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
