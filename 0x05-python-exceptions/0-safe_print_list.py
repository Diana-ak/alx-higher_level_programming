#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        print("item not found")
    else:
        print(my_list)

    return num
