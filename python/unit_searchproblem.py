import time
import sys
import random as r
import math as m
import binaryrecursive_search as test # replace X with name of script

def rand_generator(size):
    arr = []
    for i in range(size):
        arr.append(r.uniform(0, 1000))
    a = r.randint(2,10)
    b = r.randint(1,a-1)
    arr[m.floor(size*b/a)] = -1
    return arr

def sorted_generator(size):
    arr = []
    for i in range(size):
        arr.append(i)
    a = r.randint(2,10)
    b = r.randint(1,a-1)
    arr[m.floor(size*b/a)] = -1
    return arr

def runner(size):
    randarr = rand_generator(size)
    sortarr = sorted_generator(size)


def main(size, runs):
    total = runs
    successes = 0
    start = time.clock()

    index_1 = test.main(arr, -1)
    index_2 = test.main(arr2, -1)
    print("First array: index {0}, value {2}. Second array: index {1}, value {3}.".format(index_1, index_2, arr[index_1], arr2[index_2]))

    var_1 = test.main(arr, -2)
    var_2 = test.main(arr2, -2)
    print("First array: returned {0}. Second array: returned {1}.".format(var_1, var_2))
    print("Elapsed time: {0} seconds.".format(time.clock()-start))
    return 'done'



if len(sys.argv) > 1:
    main(int(sys.argv[1]), 25)
else:
    main(1000,25)
