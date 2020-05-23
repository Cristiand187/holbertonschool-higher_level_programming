#!/usr/bin/python3
"""My add integer"""


def matrix_divided(matrix, div):
    """[summary]

    Arguments:
        matrix {[type]} -- [description]
        div {[type]} -- [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        ZeroDivisionError: [description]
        TypeError: [description]

    Returns:
        [type] -- [description]
    """
    if type(matrix) not in [list] or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        + " of integers/floats")

    for rows in matrix:
        if type(rows) not in [list]:
            raise TypeError("matrix must be a matrix (list of lists)"
                            + " of integers/floats")

    len_rows = len(matrix[0])

    for rows in matrix:
        if len_rows != len(rows):
            raise TypeError("Each row of the matrix must have the same size")

    for rows in matrix:
        for elem in rows:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                + " of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    new_matrix = []

    for idx, rows in enumerate(matrix):
        new_matrix.append([])
        for cols in rows:
            new_matrix[idx].append(round(cols/div, 2))

    return new_matrix
