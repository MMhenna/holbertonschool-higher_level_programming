#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for idx, num in enumerate(matrix):
            for idx2, num2 in enumerate(matrix[idx]):
                if idx2 == len(matrix[idx]) - 1:
                    print("{:d}".format(num2))
                else:
		    print("{:d}".format(num2), end=" ")
