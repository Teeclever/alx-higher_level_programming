#!/usr/bin/python3

def no_c(my_string):
    str = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            str += letter
    return str
