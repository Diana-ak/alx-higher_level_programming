#!/usr/bin/python3
def safe_print_division(a, b):
    
    try:
        nume = int a
        deno = int b
        result = a / b

    except ZeroDivisionError:
        print("cannot divide")
    except ValueError:
        print("Not interger")
    finally:
        print("Inside result: {}".format(result))

    return result
