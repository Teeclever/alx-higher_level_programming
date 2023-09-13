#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    lists = my_list.copy()
    num_element = len(my_list)
    if idx < 0:
        return lists
    if idx >= num_element:
        return lists

    lists[idx] = element
    return lists
