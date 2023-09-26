#!/usr/bin/python3
def magic_calculation(a, b):

    res = 0

    for i in range(1, 3):
        try:
            if a < i:
                raise Exception("Too far")
            else:
                res += (a ** b) / i
        except Exception as error:
            res = b + a
            break

    return res
