#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    for i in my_dict:
        if my_dict[i] == max(my_dict.values()):
            return i
