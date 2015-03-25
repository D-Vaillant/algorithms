#!/usr/bin/env python3
''' selection_sort.py: Implements the selection sort algorithm. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

def main(array):
    for j in range(len(array)-1):
        key = array[j]
        for k in range(j+1, len(array)):
            if array[k] < key:
                temp = key
                key = array[k]
                array[k] = temp
        array[j] = key
    return array
