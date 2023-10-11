#!/usr/bin/python3
"""Log Parsing Module."""
import sys
import contextlib


def print_stats(size: int, status_codes: dict):
    """Prints the metrics.

    Args:
        size (int): The total read file size so far.
        status_codes (dict): The status codes.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":

    size = 0
    count = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            with contextlib.suppress(IndexError, ValueError):
                size += int(line[-1])
            with contextlib.suppress(IndexError):
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
        print_stats(size, status_codes)

    except KeyboardInterrupt as k:
        print_stats(size, status_codes)
        raise k
