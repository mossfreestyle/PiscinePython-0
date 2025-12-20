#!/usr/bin/env python3

import sys


def is_int(nb):

    try:
        int(nb)
        return True
    except ValueError:
        return False


try:

    if len(sys.argv) == 1:
        exit()
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif not is_int(sys.argv[1]):
        raise AssertionError("argument is not an int")
    else:
        nbr = int(sys.argv[1])
        print("I'm Even." if nbr % 2 == 0 else "I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
