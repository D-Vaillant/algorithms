#!/usr/bin/env python3
''' priority_queue_heap.py: Implements a priority queue data structure based off
                       of heaps. '''

__author__ = "David Vaillant"
__credits__ = "LCRS"

import math

class p_queue:
    def __init__(self, input_list):
        self.size = len(input_list)
        self.queue = input_list

class d_p_queue(p_queue):
    def __init__(self, input_list):
        super(d_p_queue, self).__init__(input_list)
        self.queue = build_descending_queue(self).queue

def left(i): 
    return (2*(i+1))-1

def right(i): 
    return 2*(i+1)
    
def parent(i): return math.ceil(i/2)-1

def build_descending_queue(prior):
    i = math.floor(prior.size/2)
    while i >= 0:
       prior = descend_queue(prior, i)
       i = i-1
    return prior

def descend_queue(p, i):
    l = left(i)
    r = right(i)
    if l < p.size and p.queue[l][1] > p.queue[i][1]:
        greatest = l
    else: greatest = i
    if r < p.size and p.queue[r][1] > p.queue[greatest][1]:
        greatest = r
    if greatest != i:
        p.queue[i], p.queue[greatest] = p.queue[greatest], p.queue[i]
        descend_queue(p, greatest)
    return p

# takes a priority queue, returns true if it has a max heap structure.
def is_descending_queue(p):
    i = p.size-1
    while i > 0:
        if p.queue[i][1] > p.queue[parent(i)][1]: return False
        i = i-1
    return True
