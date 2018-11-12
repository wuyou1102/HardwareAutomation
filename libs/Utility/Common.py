# -*- encoding:UTF-8 -*-


def remove_builtins_from_list(lst):
    return [x for x in lst if not x.startswith('__') or not x.endswith('__')]