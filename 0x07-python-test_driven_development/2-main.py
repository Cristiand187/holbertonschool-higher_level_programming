#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix_divided(matrix, 3))
# print(matrix)

matrix = []
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e.args[0])

matrix = [[1, 2, 4], [2, 3]]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e.args[0])


matrix = [[1, '', 4], [2, 3]]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e.args[0])
print(matrix_divided(matrix, 3))
