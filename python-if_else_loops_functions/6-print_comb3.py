#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{}".format(f"{i}{j}"), end=", " if i < 8 else "\n")
