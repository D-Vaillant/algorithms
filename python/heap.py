import math

class heap:
    def __init__(self, arr):
        self.eapsize = len(arr)
        self.eap = arr

def left(i): 
    return (2*(i+1))-1

def right(i): 
    return 2*(i+1)
    
def parent(i): return math.ceil(i/2)-1

def build_max_heap(arr):
    h = heap(arr)
    i = math.floor(len(arr)/2)
    while i >= 0:
       h = max_heapify(h, i)
       i = i-1
    return h

def max_heapify(h, i):
    l = left(i)
    r = right(i)
    if l < h.eapsize and h.eap[l] > h.eap[i]:
        greatest = l
    else: greatest = i
    if r < h.eapsize and h.eap[r] > h.eap[greatest]:
        greatest = r
    if greatest != i:
        temp = h.eap[i]
        h.eap[i] = h.eap[greatest]
        h.eap[greatest] = temp
        max_heapify(h, greatest)
    return h

# takes a heap, returns true if it is a max heap.
def is_max_heap(h):
    i = h.eapsize-1
    while i > 0:
        if h.eap[i] > h.eap[parent(i)]: return False
        i = i-1
    return True
