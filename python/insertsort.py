#!/usr/bin/env python3
''' insertsort.py: Implements the insertion sort algorithm. Includes some
                   error-prevention. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

def main(array):
    try:
        for x in range(1, len(array)):
            y = x-1
            key = array[x]
            while y > -1 and array[y] > key:
                array[y+1] = array[y]
                y = y - 1
            array[y+1] = key

    except TypeError:
        print("Error, invalid type at some point.")

    return array
