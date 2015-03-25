#!/usr/bin/env python3
''' heap.py: Implementation of the heap data structure and several methods for
             use on heaps. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

import math

class heap:
    def __init__(self, arr):
        self.eapsize = len(arr)
        self.eap = arr

    def build_max_heap(self):
        i = math.floor(self.eapsize/2)
        while i >= 0:
           self = self.max_heapify(i)
           i = i-1
        return "Complete."

    def max_heapify(self, i):
        l = left(i)
        r = right(i)
        if l < self.eapsize and self.eap[l] > self.eap[i]:
            greatest = l
        else: greatest = i
        if r < self.eapsize and self.eap[r] > self.eap[greatest]:
            greatest = r
        if greatest != i:
            self.eap[i], self.eap[greatest] = self.eap[greatest], self.eap[i]
            self.max_heapify(greatest)
        return self

# returns true if heap is a max heap
    def is_max_heap(self):
        i = self.eapsize-1
        while i > 0:
            if self.eap[i] > self.eap[parent(i)]: return False
            i = i-1
        return True

class max_heap(heap):
    def __init__(self, arr):
        super(max_heap, self).__init__(arr)
        self.super(max_heap, self).build_max_heap()

def left(i): 
    return (2*(i+1))-1

def right(i): 
    return 2*(i+1)
    
def parent(i): return math.ceil(i/2)-1
