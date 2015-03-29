#!/usr/bin/env python3
''' countingsort.py: Implements the counting sort algoritm. main automatically
                     finds the max value and plugs it into the generalized
                     main for simplicity (at the cost of performance).'''

__author__ = "David Vaillant"
__credits = "LCRS"

def gen_main(A, k):
    C = [0]*(k+1)
    B = [None]*len(A)
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(k):
        C[i+1] = C[i] + C[i+1]
    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

def main(A):
    return gen_main(A, max(A))
