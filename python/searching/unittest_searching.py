#!/usr/bin/env python3
""" unittest_searching.py: Unit test for the search problem.
    Creates an arbitrary number of unsorted arrays containing random integers,
    inserts a randomly generated target in a random index for each array, and
    runs the imported search algorithm to find the targets.

    Checks if the index returned corresponds to the target and reports the
    average, worst, and best times. """ 

__author__ = "David Vaillant"

import unittest, time, sys
import random as r
import math as m
from statistics import mean

class SearchTester(unittest.TestCase): 
    search = None
    size = 1000
    runs = 10

    def meta_tester(self, array_type, succeed = True):
        """ Generates an array and searches it. 
        
            Generalizes the common elements of the various tests run - 
            each test creates a specific kind of array and either attempts
            to find or fail to find a given element. """
        arr, index_target = getattr(self, array_type+"_generator")()

        search_target = -1 if succeed else -2

        found_index = SearchTester.search(arr, search_target)

        time_taken = None
        # Will remove the index operation at some later point.
        return (found_index is not None, time_taken)[0]
 
        """
        # Sorry, clock.

        start = time.clock()
        found_index = self.search(arr, search_target)
        time_taken = time.clock() - start
        """

        """
        # Currently, not sure how to implement timing under a unittest
        # framework. As such, this section is commented out.

        if search_target == -1:
            if found_index is not None and arr[found_index] == search_target:
                return found_index == index_target#, time_taken
            else:
                return False#, -1
        else:
            if found_index is None:
                return True#, time_taken
            else:
                return False#, -1
        """
           
    def test_random_arr_SUCCESS(self):
        self.assertTrue(self.meta_tester("rand"))
    
    def test_sorted_arr_SUCCESS(self):
        self.assertTrue(self.meta_tester("sorted"))

    def tester_revsorted_arr_SUCCESS(self):
        self.assertTrue(self.meta_tester("reverse_sorted")) 

    def test_random_arr_FAIL(self):
        self.assertFalse(self.meta_tester("rand", succeed = False))

    def test_sorted_arr_FAIL(self):
        self.assertFalse(self.meta_tester("sorted", succeed = False))

    def test_revsorted_arr_FAIL(self):
        self.assertFalse(self.meta_tester("reverse_sorted", succeed = False))

    @classmethod
    def rand_generator(cls):
        arr = [r.randrange(0, cls.size) for _ in range(cls.size)]

        target = r.randrange(0, cls.size)
        arr[target] = -1
        
        return arr, target

    @classmethod
    def sorted_generator(cls):
        arr = list(range(cls.size))
        arr[0] = -1
        return arr, 0
        
    @classmethod
    def reverse_sorted_generator(cls):
        arr = list(reversed(range(cls.size)))
        arr[-1] = -1    
        return arr, cls.size-1   

    """
    Unimplemented code for timing and percentages.
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
    """

"""
if len(sys.argv) > 1:
    main(int(sys.argv[1]), 100)
else:
    main(1000, 100)
    """
