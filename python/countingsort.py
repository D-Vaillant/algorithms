#!/usr/bin/env python3
''' countingsort.py: Implements the counting sort algorithm. main automatically
                     finds the max value and plugs it into the generalized
                     main for simplicity (at the cost of performance).'''

__author__ = "David Vaillant"
__credits = "CLRS"

def gen_main(A, k):
    """ Takes a list A and a value k such that i <= k for i in A.
        Returns a sorted list. """
    C = [0]*(k+1)
    B = [None]*len(A)
    for j in A:
        C[j] += 1 # Turns C into a Counter for A.
    for i in range(k):
        C[i+1] = C[i] + C[i+1] 
    for j in reversed(A):
        B[C[j]-1] = j
        C[j] -= 1
    return B

def main(A):
    return gen_main(A, max(A))
