'''#!/usr/bin/python'''


def flatten_list(lst):
    if not isinstance(lst, list):
        return -1
    else:
        new_lst = []
        flatten_recursive_helper(lst, new_lst)
        return new_lst


def flatten_recursive_helper(lst, new_lst):
    for item in lst:
        if not isinstance(item, list):
            if type(item) == type(1):
                new_lst.append(item)
            else:pass
        else:
            flatten_recursive_helper(item, new_lst)
