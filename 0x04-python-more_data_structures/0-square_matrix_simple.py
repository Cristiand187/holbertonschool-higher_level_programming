#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for idx, row in enumerate(matrix):
        new_matrix.append([])
        for col in row:
            new_matrix[idx].append(col*col)

    return (new_matrix)
