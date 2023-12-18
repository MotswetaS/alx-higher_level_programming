#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        main = a / b
    except (ZeroDivisionError):
        main = None
    finally:
        print("Inside result: {}".format(main))
        return main
