#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads the content of a file and prints it.

    Args:
    filename (str): The name of the file to read. Default is an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

