#!/usr/bin/env python3
''' linear_search.py: Implements the linear search algorithm. '''

__author__ = "David Vaillant"
__credits__ = "CLRS, Chapter 2.1"

from unittest_searching import SearchTester
import unittest

def linear_search(array, v):
    """ Solution for 2.1-3. """
    for index, value in enumerate(array):
        if value == v: return index
    else: return None

if __name__ == "__main__":
    SearchTester.search = linear_search
    unittest.main()
