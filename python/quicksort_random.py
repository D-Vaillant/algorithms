#!/usr/bin/env python3
''' quicksort_random.py: Implements the quicksort algorithm, choosing a 
                         random element of the array to be the pivot. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

import quicksort
import random

def main(arr):
    remain(arr, 0, len(arr)-1)
    return arr

def remain(arr, p, r):
    if p < r:
        q = partition_random(arr, p, r)
        remain(arr, p, q-1)
        remain(arr, q+1, r)
    return arr

def partition_random(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return quicksort.partition(A, p, r)

