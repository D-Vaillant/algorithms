#!/usr/bin/env python3
''' bucketsort_interval.py: Implements the bucket sort algorithm over a list
                            with elements taken from [0, 1).
                            Depends on some other sort algorithm (insert used).
'''
__author__ = "David Vaillant"
__credits__ = "LCRS"

from math import floor
import insertsort as sort

def main(A):
    """" Sorts a list A of size n with elements taken from [0, 1). """
    n = len(A)
    B = [list() for x in range(n)]
    for i in A:
        B[floor(n*i)].append(i)
    for i in range(n):
        sort.main(B[i])
    return sum(B, []) # Union operation on the list. 
