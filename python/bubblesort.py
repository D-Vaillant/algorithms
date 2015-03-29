#!/usr/bin/env python3
''' bubblesort.py: Implements the bubble sort algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS"

def main(A):
    for i in range(len(A)-1):
        for j in reversed(range(i+1, len(A))):
            if A[j] < A[j-1]:
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
    return A