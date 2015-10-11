#!/usr/bin/env python3
''' heapsort.py: Takes an array, turns it into a max heap, and implements
                 the heapsort algorithm in order to return a sorted array.'''

__author__ = "David Vaillant"
__credits__ = "CLRS"

import math
from heap import Heap, Max_Heap

def main(arr):
    h = Max_Heap(arr)
    for i in reversed(range(1, len(arr))):
        h.eap[0], h.heap[i] = h.eap[i], h.eap[0]
        h.eapsize = h.eapsize - 1
        max_heapify(h, 0)
    return h.eap
