#!/usr/bin/env python3
''' insertsort_recursive.py: A recursive implementation of the insertion sort
                             algorithm. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

def main(A):
    if len(A) == 1:
        return A
    else:
        return linear_merge(main(A[:len(A)-1]), A[len(A)-1])



def linear_merge(A, x):
    i = len(A)-1
    A.append(x)
    while i >= 0 and A[i] > x:
        A[i+1] = A[i]
        i = i-1
    A[i+1] = x
    return A
