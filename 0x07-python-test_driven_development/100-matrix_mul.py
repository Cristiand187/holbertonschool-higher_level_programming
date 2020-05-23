#!/usr/bin/python3
"""
    Funtion mul two matrix
"""


def matrix_mul(m_a, m_b):
    """[summary]

    Arguments:
        m_a {[type]} -- [description]
        m_b {[type]} -- [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        ValueError: [description]
        ValueError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type] -- [description]
    """

    if type(m_a) not in [list]:
        raise TypeError("m_a must be a list")
    if type(m_b) not in [list]:
        raise TypeError("m_b must be a list")
    for elem in m_a:
        if type(elem) not in [list]:
            raise TypeError("m_a must be a list of lists")
    for elem in m_a:
        if type(elem) not in [list]:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for rows in m_a:
        for elem in rows:
            if type(elem) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for rows in m_b:
        for elem in rows:
            if type(elem) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    len_rows = len(m_a[0])

    for rows in m_a:
        if len_rows != len(rows):
            raise TypeError("each row of m_a must be of the same size")

    len_rows = len(m_b[0])

    for rows in m_b:
        if len_rows != len(rows):
            raise TypeError("each row of m_b must be of the same size")

    matrix_new = []

    for i in range(len(m_a)):
        matrix_new.append([])
        for j in range(len(m_b[0])):
            elem_r = 0
            for k in range(len(m_b)):
                elem_r += m_a[i][k] * m_b[k][j]
            matrix_new[i].append(elem_r)
    return matrix_new
