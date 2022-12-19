#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """

    number = 0

    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            number += 1
        except (ValueError, TypeError):
            idx += 1
            continue
        print("")
        return number
