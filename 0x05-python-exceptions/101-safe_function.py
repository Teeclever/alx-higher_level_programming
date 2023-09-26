#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)

    except (ZeroDivisionError, TypeError, IndexError, ValueError) as error:
        print("Exception: {}".format(str(error)), file=sys.stderr)
        return None

    else:
        return result
