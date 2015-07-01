#!/usr/bin/env python3
''' binaryiterative_search.py: Uses a binary search algorithm on an already
                               sorted list to return an index. main function
                               presorts the list using mergesort. Iterative.
'''

__author__ = "David Vaillant"
__credits__ = "CLRS"

import math
import mergesort

def main(A, v):
    return riskymain(mergesort.main(A), v)
    
def riskymain(A, v):
    """ If v is in A, returns i s.t. A[i] = v. Relies on A being sorted. """
    a = 0
    b = len(A)-1
    i = math.floor((a+b)/2)
    while b-a > 1 and A[i] != v:
        if A[i] > v:
            temp = i
            i = math.floor((a+b)/2)
            b = temp
        else:
            temp = i
            i = math.floor((a+b)/2)
            a = temp
    if A[i] == v:
            return i
    else: return None
