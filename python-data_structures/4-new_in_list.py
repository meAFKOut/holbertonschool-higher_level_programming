#!/usr/bin/python3
def new_in_list(lost, pon, kol):
    if pon >= len(lost) or pon < 0:
        return lost
    lost = lost[:]
    lost[pon] = kol
    return new_list
