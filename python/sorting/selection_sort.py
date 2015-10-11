cat#!/usr/bin/env python3
''' selection_sort.py: Implements the selection sort algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

def main(array):
    for j, key in enumerate(array):
        for laterVal in array[j+1:]:
            if laterVal < key:
                key, laterVal = laterVal, key
        array[j] = key
    return array
