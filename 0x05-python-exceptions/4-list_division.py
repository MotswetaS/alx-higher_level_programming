#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            main = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            main = 0
        except ZeroDivisionError:
            print("division by 0")
            main = 0
        except IndexError:
            print("out of range")
            main = 0
        finally:
            n_list.append(main)
    return n_list
