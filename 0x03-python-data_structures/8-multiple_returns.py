#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        a = 0
        b = None
        return (a, b)

    a = len(sentence)
    b = sentence[0]
    return (a, b)
