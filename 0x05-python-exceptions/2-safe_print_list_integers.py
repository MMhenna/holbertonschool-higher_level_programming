#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for idx, num in enumerate(my_list):
        try:
            if x > idx:
                print("{:d}".format(num), end='')
                counter += 1
        except IndexError:
            return counter
        except (ValueError, TypeError):
            continue
    
    print()
    return counter
