#!/usr/bin/python3
"""[summary]"""


def pascal_triangle(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    list_pascal = []
    if n <= 0:
        return list_pascal
    for idx in range(n):
        list_pascal.append([])
        i = 0
        while i <= idx:
            value = sum(list_pascal[idx-1][i-1:i+1])
            list_pascal[idx].append(value if value != 0 else 1)
            i += 1
    return list_pascal
