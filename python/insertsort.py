#!/usr/bin/env python3
''' insertsort.py: Implements the insertion sort algorithm. Includes some
                   error-prevention. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

V = False

def main(array):
    try:
        for index, value in enumerate(array[1:]):
            if V: print("Index is {}, value is {}. Array[index] is {}.".format(
                                                   index, value, array[index]))

            while index >= 0 and array[index] > value:
                if V: print("Swapping {} with {}.".format(
                            array[index], array[index+1]))
                array[index+1] = array[index]
                index -= 1

            if V: print("Final swap: {} with {}.".format(array[index+1], value))

    except TypeError:
        print("Error, invalid type at some point.")

    return array
