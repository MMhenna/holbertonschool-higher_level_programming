#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sums = 0
    div = 0
    for tup in my_list:
        sums += tup[0] * tup[1]
        div += tup[1]
    return sums / div
