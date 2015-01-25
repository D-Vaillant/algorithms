import math
import mergesort

def main(A, v):
    return riskymain(mergesort.main(A), v)
    
def riskymain(A, v):
    a = 0
    b = len(A)-1
    i = math.floor((a+b)/2)
    while b-a > 1 and A[i] != v:
        if A[i] > v:
            temp = i
            i = math.floor((a+b)/2)
            b = temp
        else:
            temp = i
            i = math.floor((a+b)/2)
            a = temp
    if A[i] == v:
            return i
    else: return None
