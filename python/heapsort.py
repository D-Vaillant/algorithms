import math
from heap import *

def main(arr):
    h = build_max_heap(arr)
    for i in reversed(range(1, len(arr))):
        temp = h.eap[0]
        h.eap[0] = h.eap[i]
        h.eap[i] = temp
        h.eapsize = h.eapsize - 1
        max_heapify(h, 0)
    return h.eap
