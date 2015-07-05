#!/usr/bin/env python3
''' linear_search.py: Implements the linear search algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

def main(array, v):
    for index, value in enumerate(array):
        if value == v: return index
    else: return None
