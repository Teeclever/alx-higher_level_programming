#!/usr/bin/python3
"""
Thia module contains the definition of the function `matrix_divided()`.
"""


def matrix_divided(matrix, div):
    """Divides all numbers in a matrix by a number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int): Number to divide by.

    Raises:
        TypeError: If matrix is not a list.
        TypeError: If matrix is not a list of lists.
        TypeError: If all lists in the matrix are not the same size.
        TypeError: If any element of matrix is not an int or float.
        ZeroDivisionError: If num is 0.

    Returns:
        list of lists: New matrix with elements divided.
    """
    err_lol = "matrix must be a matrix (list of lists) of integers/floats"
    err_row = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not all(
        (isinstance(inner, list) for inner in matrix)
    ):
        raise TypeError(err_lol)

    row_size = len(matrix[0])
    for inner in matrix:
        if any(type(e) not in (int, float) for e in inner):
            raise TypeError(err_lol)
        if len(inner) != row_size:
            raise TypeError(err_row)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(e/int(div), 2) for e in inner] for inner in matrix]
