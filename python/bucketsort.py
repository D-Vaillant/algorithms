#!/usr/bin/env python3
''' bucketsort.py: Implements the bucket sort algorithm over a list
                   with elements taken from some specified interval.
                   Depends on some other sort algorithm (insert used).
'''
__author__ = "David Vaillant"
__credits__ = "LCRS"

from math import floor, ceil   
import insertsort as sort

def main(A):
    inval = (floor(min(A)), ceil(max(A)) + 1)
    return gen_main(A, inval)

def gen_main(A, interval):
    n = len(A)
    B = [list() for x in range(n)]

    # defines a surjection from the interval to range(n)
    def f(x):
        return floor(n*((x-interval[0])/(interval[1]-interval[0])))

    for i in range(n):
        B[floor(f(A[i]))].append(A[i])
    for i in range(n):
        sort.main(B[i])
    return sum(B, [])
