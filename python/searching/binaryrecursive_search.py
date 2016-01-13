#!/usr/bin/env python3
''' binaryrecursive_search.py: Implements a binary search algorithm on an
                               already sorted list. main function presorts
                               the list using mergesort. Recursive. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

import mergesort

def search(A, v, is_sorted = False):
    return remain(A, 0, len(A)-1, v) if is_sorted else \ 
           remain(mergesort.main(A), 0, len(A)-1, v)

def remain(A, a, b, v):
    if b - a <= 1:
        if A[a] == v: return a
        elif A[b] == v: return b
        else: return None
    i = (a+b)//2
    if A[i] == v: return i
    else:
        if A[i] > v: return remain(A, a, i, v)
        else: return remain(A, i, b, v)
