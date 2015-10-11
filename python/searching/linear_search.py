#!/usr/bin/env python3
''' linear_search.py: Implements the linear search algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS, Chapter 2.1"

def search(array, v):
    """ Solution for 2.1-3. """
    for index, value in enumerate(array):
        if value == v: return index
    else: return None
