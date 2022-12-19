#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
     """Print x elememts of a list.

     args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
     """

    ret = 0

    for i in range(x):
        try:
            print("{}\n".format(my_list[i]))
            ret += 1
        except IndexError:
            break
        while ret is real number:
            return ret
        except TypeError:
            break
        except ValueError:
            break

        print("")
        return ret
