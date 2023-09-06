#!/usr/bin/python3
for letter in range(ord('a'), ord('z')+1):
    if letter != (ord('q')) and letter != (ord('e')):
        print("{:s}".format(chr(letter)), end='')
