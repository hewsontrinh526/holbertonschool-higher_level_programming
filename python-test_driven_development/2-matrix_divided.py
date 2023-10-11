#!/usr/bin/python3
"""
Module: 2-matrix_divided.py

Function: matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: Takes a square matrix
    and divides each element by a specific divisor

    Args: 
    matrix: A matrix that is being divided
    div: An integer or a float that is used to divide the matrix elements

    Returns:
    A new matrix with all elements divided
    """
    err_msg_1 = "matrix must be a matrix (list of lists) of integers/float"
    err_msg_2 = "each row of the matrix must be the same size"
    err_msg_3 = "div must be a number"
    err_msg_4 = "division by zero"
    row_size = len(matrix[0])
    num_row = len(matrix)
    divided_matrix = [[0 for i in range(row_size)] for i in range(len(matrix))]

    if type(matrix) is not list:
        raise TypeError(err_msg_1)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_msg_1)
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError(err_msg_1)
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(err_msg_2)
    if type(div) is not int and type(div) is not float:
        raise TypeError(err_msg_3)
    if div == 0:
        raise ZeroDivisionError(err_msg_4)
    for i in range(num_row):
        for j in range(row_size):
            divided_matrix[i][j] = round(matrix[i][j] / div, 2)
    return divided_matrix
