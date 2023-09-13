#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)

    for row in matrix:
        num_elements = len(row)
        lens = 0

        for i in row:
            if lens < num_elements - 1:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
            lens += 1
        print()
