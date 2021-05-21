#!/usr/bin/python3

"""2-matrix_divid: module that divides all elements in a matrix
by the div parameter, returns a new list matrix

"""

def matrix_divided(matrix, div):
    """ Devide all elements of 'matrix' by 'div'

    Args:
        matrix: a list of same size lists of integers or floats
        div: a non zero int or float

    Returns:
        a new divided matrix

    Raises:
        TypeError: if any of the matrix elements is not an integer or a float;
                if the matrix rows are not all equal;
                if 'div' is not a number
        ZeroDivisionError: if 'div' is a 0
    """

    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    row_len = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        if any(map(lambda el: (type(el) is not int and type(el) is not float), row)):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    res = list(map(lambda L: list(map(lambda el: round(el / div, 2), L)), matrix))
    return res