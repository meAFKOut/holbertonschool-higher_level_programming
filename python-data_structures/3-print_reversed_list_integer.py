#!/usr/bin/python3
def print_reversed_list_integer(lost=[]):
    if isinstance(lost, list):
        lost.reverse()
        for i in lost:
            print("{:d}".format(i))
