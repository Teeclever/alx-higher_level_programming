#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for num in range(x):
            print("{}".format(my_list[num]), end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
