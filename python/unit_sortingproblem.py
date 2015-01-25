import sys
import random as r
import heapsort as test # replace X with name of script

def main(size, runs):
    glass = True
    for j in range(runs):
        a = generator(size)
        b = isIncorrect(a)
        if b[0]:
            print("Failed at indexes {0}, {1}.".format(b[1]-1,b[1]))
            #print(a)
            glass = False
    if glass: print("All arrays successfully sorted.")

def generator(size):
    arr = []
    for i in range(size):
        arr.append(r.uniform(0, 100000)) 

    return test.main(arr)

def isIncorrect(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return True, i
    return False, -1

main(5000, 30)
