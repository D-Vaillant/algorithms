#!/usr/bin/env python3
''' linear_search.py: Implements the linear search algorithm. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

def main(array, v):
    i = 0
    while i < len(array) and array[i] != v:
        i = i+1
    if i >= len(array):
        return None
    else:
        return i
