import math

def easy_main(A, v):
    return main(A, v, 0, len(A)-1)

def main(A, a, b, v):
    i = math.ceiling((a+b)/2)
    if b - a <= 1:
        return b
    if A[i] < z: return main(A, i, b, z)
    else: return main(A, a, i, z)
