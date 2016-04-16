#!/usr/bin/env python3
""" insertsort.py: Implements the insertion sort algorithm. """

__author__ = "David Vaillant"
__credits__ = "CLRS, Chapter 2.1"

V = False

def main(array):
    """ Takes an array of values with a > and == operator, sorts it. """
    # Starts with 0, array[1].
    for index, value in enumerate(array[1:]):
        if V: print("Index is {}, value is {}. Array[index] is {}.".format(
                                               index, value, array[index]))

        # Loops through the previous indices if their value is greater than
        # VALUE. If so, swap value with value of next index.
        while index >= 0 and array[index] > value:
            if V: print("Swapping {} with {}.".format(
                        array[index], array[index+1]))
            array[index+1] = array[index]
            # Decrement to previous index.
            index -= 1
        array[index+1] = value

        if V: print("Final swap: {} with {}.".format(array[index+1], value))

    return array

def reversed_main(array):
    """ Toy solution for 2.1-2. """
    # Starts with 0, array[1].
    for index, value in enumerate(array[1:]):
        if V: print("Index is {}, value is {}. Array[index] is {}.".format(
                                               index, value, array[index]))

        # Loops through the previous indices if their value is greater than
        # VALUE. If so, swap value with value of next index.
        while index >= 0 and array[index] < value:
            if V: print("Swapping {} with {}.".format(
                        array[index], array[index+1]))
            array[index+1] = array[index]
            # Decrement to previous index.
            index -= 1
        array[index+1] = value

        if V: print("Final swap: {} with {}.".format(array[index+1], value))

    return array
