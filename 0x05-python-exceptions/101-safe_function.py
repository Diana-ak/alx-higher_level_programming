#!/usr/bin/python3

from sys import stderr
def safe_function(fct, *args):
    """ Executes a function safetly.

    Args:
        fct: Function to execute
        args: arguemnts in teh function.
    Return:
        none on failure
        result of function.
    """

    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return None
    else:
        return res
