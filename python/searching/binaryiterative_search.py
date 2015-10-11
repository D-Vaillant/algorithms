#!/usr/bin/env python3
''' binaryiterative_search.py: Uses a binary search algorithm on an already
                               sorted list to return an index. main function
                               presorts the list using mergesort. Iterative.
'''

__author__ = "David Vaillant"
__credits__ = "CLRS"

from math import floor 
import mergesort

def main(A, v):
    return riskymain(mergesort.main(A), v)
    
def riskymain(A, v):
    """ If v is in A, returns i s.t. A[i] = v. Relies on A being sorted. """
    a = 0
    b = len(A)-1
    i = (a+b)//2
    while b-a > 1 and A[i] != v:
        if A[i] > v:
            b, i = i, (a+b)//2
        else:
            a, i = i, (a+b)//2
    if A[i] == v:
        return i
    else: return None
