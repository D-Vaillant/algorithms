#!/usr/bin/env python3
""" unit_searchproblem.py: Unit test for the search problem.
    Creates an arbitrary number of unsorted arrays containing random integers,
    inserts a randomly generated target in a random index for each array, and
    runs the imported search algorithm to find the targets.

    Checks if the index returned corresponds to the target and reports the
    average, worst, and best times. """ 

__author__ = "David Vaillant"

import time
import sys
import random as r
import math as m
import binaryrecursive_search as test # replace X with name of script
from statistics import mean

class GeneratorWrapper():
    @staticmethod
    def rand_generator(size):
        arr = [r.randrange(0, size) for _ in range(size)]

        target = r.randrange(0, size)
        arr[target] = -1
        
        return arr, target

    @staticmethod
    def sorted_generator(size):
        arr = list(range(size))
        arr[0] = -1
        return arr, 0
        
    @staticmethod
    def reverse_sorted_generator(size):
        arr = list(reversed(range(size)))
        arr[-1] = -1    
        return arr, size-1   

def runner(size, gen_name, succeed=True):
    arr, index_target = getattr(GeneratorWrapper, gen_name+"_generator")(size)

    search_target = -1 if succeed else -2
    
    start = time.clock()
    found_index = test.search(arr, search_target)
    time_taken = time.clock() - start
    
    if search_target == -1:
        if found_index is not None and arr[found_index] == search_target:
            return found_index == index_target, time_taken
        else:
            return False, -1        
    else:
        if found_index is None:
            return True, time_taken
        else:
            return False, -1

def main(size, runs):
    types_dict = {
        "rand":            True,
        "sorted":          True,
        "reverse_sorted":  True,
        }
        
    types_detail = { x:[[],[]] for x in types_dict if types_dict[x] }
    
    for type, detail_list in types_detail.items():
        for _ in range(runs):
            result, time = runner(size, type)
            detail_list[0].append(result)
            detail_list[1].append(time)
            
        percent = detail_list[0].count(True)/runs
        avg_time = mean([x for x in detail_list[1] if x > 0])
        print("Results for " + type + ":")
        print("Percentage success: ", percent)
        print("Average time: ", avg_time)
        print()
     
    return 0



if len(sys.argv) > 1:
    main(int(sys.argv[1]), 100)
else:
    main(1000, 100)
