#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a >= 2 and len_b >= 2:
        c = tuple_a[0] + tuple_b[0]
        d = tuple_a[1] + tuple_b[1]
    elif len_a >= 2 and len_b == 1:
        c = tuple_a[0] + tuple_b[0]
        d = tuple_a[1]
    elif len_a >= 2 and len_b == 0:
        c = tuple_a[0]
        d = tuple_a[1]
    elif len_a == 1 and len_b >= 2:
        c = tuple_a[0] + len_b[0]
        d = len_b[1]
    elif len_a == 1 and len_b == 1:
        c = tuple_a[0] + tuple_b[0]
        d = 0
    elif len_a == 0 and len_b == 1:
        c = len_b[0]
        d = 0
    elif len_a == 1 and len_b == 0:
        c = 0
        d = len_a[0]
    elif len_a == 0 and len_b == 0:
        c = 0
        d = 0

    return (c, d)
