#!/usr/bin/python3
def replace_in_list(list, pon, lol):
    if pon >= len(list) or pon < 0:
        return list
    list[pon] = lol
    retu list
