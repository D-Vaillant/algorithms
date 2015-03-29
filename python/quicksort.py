#!/usr/bin/env python3
''' quicksort.py: Implements the quicksort algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

def main(arr):
    remain(arr, 0, len(arr)-1)

def remain(arr, p, r):
    if p<r:
        q = partition(arr, p, r)
        remain(arr, p, q-1)
        remain(arr, q+1, r)
    return arr

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
        print(A)
    A[i+1], A[r] = A[r], A[i+1]
    print(A)
    return i+1


