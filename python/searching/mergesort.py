#!/usr/bin/env python3
''' mergesort.py: Implements the merge sort algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

import math

def remain(A, p, r):
    if p<r:
        q = math.floor((p+r)/2)
        remain(A, p, q)
        remain(A, q+1, r)
        merge(A, p, q, r)
    return A

def main(A):
    return remain(A, 0, len(A)-1)

def merge(A, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q
    L = []
    R = []
    for i in range(n_1):
        L.append(A[p+i])
    for j in range(n_2):
        R.append(A[q+j+1])
    i = 0
    j = 0
    for k in range(p, r+1):
        if n_1 != 0 and (n_2 == 0 or L[i] <= R[j]):
            A[k] = L[i]
            i = i+1
            n_1 = n_1 - 1
        else:
            A[k] = R[j]
            j = j+1
            n_2 = n_2 - 1

