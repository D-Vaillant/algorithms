#!/usr/bin/env python3
""" unit_sortingproblem.py: Unit test for the sorting problem. 
        Creates an arbitrary number of unsorted arrays containing random integers
        and sorts them using the imported algorithm. Reports worst, best, and 
        average time and whether or not any of the arrays are improperly sorted"""

from __future__ import print_function
from importlib import import_module

import sys, time
import random as r

__author__ = "David Vaillant"

def main(sort_func, size = 5000, runs = 30):
    glass = True
    time_arr = []
    for j in range(runs):
        a = [r.randrange(1000) for x in range(size)]
        begin = time.time()
        a = test.main(a)
        elapsed = time.time() - begin
        if isNotSorted(a):
            glass = False
        else:
            time_arr.append(elapsed)
    if glass: print("All arrays successfully sorted.")
    return time_arr

def generator(size):
    arr = [r.randrange(1000) for x in range(size)]

    return test.main(arr)

def isNotSorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return i
    return 0

if __name__ == "__main__":
    try:
        test = import_module(sys.argv[1])
    except IndexError:
        test = import_module("quicksort")

    times = main(test.main, 5000, 30)
    print("Worst-time was {}".format(max(times)))
    print("Best-time was {}.".format(min(times)))
    print("Average-time was {}.".format(sum(times)/len(times)))
