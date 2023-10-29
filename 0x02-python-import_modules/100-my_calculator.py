#!/usr/bin/python3

from calculator_1 import add, mul, div, sub
from sys import argv, stderr, exit


if __name__ == "__main__":

    store = argv
    store.pop(0)

    count = len(store)
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    result = 0
    a = int(store[0])
    operator = store[1]
    b = int(store[2])

    match operator:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '/':
            result = div(a, b)
        case '*':
            result = mul(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    print(f"{a} {operator} {b} = {result}")
