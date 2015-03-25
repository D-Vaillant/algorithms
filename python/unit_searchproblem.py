#!/usr/bin/env python3
''' unit_searchproblem.py: Unit test for the search problem. '''
''' Creates an arbitrary number of unsorted arrays containing random integers,
    inserts a randomly generated target in a random index for each array, and
    runs the imported search algorithm to find the targets.
    Checks if the index returned corresponds to the target and reports the
    average, worst, and best times. '''

__author__ = "David Vaillant"

import time
import sys
import random as r
import math as m
import binaryrecursive_search as test # replace X with name of script

def rand_generator(size):
    arr = []
    for i in range(size):
        arr.append(r.randint(0,size))
    return arr

def sorted_generator(size):
    arr = []
    for i in range(size):
        arr.append(i)
    return arr

def runner(size):
    randarr = rand_generator(size)
    sortarr = sorted_generator(size)


def main(size, runs):
    total = runs
    successes = 0
    start = time.clock()

    index_1 = test.main(arr, -1)
    index_2 = test.main(arr2, -1)
    print("First array: index {0}, value {2}. Second array: index {1}, value {3}.".format(index_1, index_2, arr[index_1], arr2[index_2]))

    var_1 = test.main(arr, -2)
    var_2 = test.main(arr2, -2)
    print("First array: returned {0}. Second array: returned {1}.".format(var_1, var_2))
    print("Elapsed time: {0} seconds.".format(time.clock()-start))
    return 'done'



if len(sys.argv) > 1:
    main(int(sys.argv[1]), 25)
else:
    main(1000,25)
