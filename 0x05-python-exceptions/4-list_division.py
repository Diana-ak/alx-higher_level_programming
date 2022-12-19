#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []

        for i in range(list_length):
            result = my_list_1[i] / my_list_2[i]
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    except (ValueError, TypeError):
        print ("wrong type")
    finally:
        new_list.append(result)

    return new_list