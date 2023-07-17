#!/usr/bin/python3

"""
2-matrix_divided
"""

def matrix_divided(matrix, div):
    """
    divides matrix by div

    Args:
        matrix (list): list containing lists
        div (int): number to divide by

    Returns:
        list: matrix

    """

    new_matrix = []

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        new_row = []
        for j in matrix[i]:
            if isinstance(j, (int, float)):
                new_row.append(round(j/div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        new_matrix.append(new_row)

    return new_matrix

