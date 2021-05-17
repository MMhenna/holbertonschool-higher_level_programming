#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(0, list_length):
        try:
            val = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            val = 0
            pass
        except ZeroDivisionError:
            print("division by 0")
            val = 0
            pass
        except IndexError:
            print("out of range")
            val = 0
            pass
        finally:
            new_list.append(val)
    return new_list