## Permutation sort
"""
Given an array or a list of integers, find their permutations.
Permutation is any arrangement of a given element. 
Iterate through different permutation values and return the permutation that is sorted. 
"""

from itertools import permutations 

def permutation_sort(arr):
    """
    Given an array/list of integers, 
    Find their permutations and return the sorted permutation
    """

    permu = permutations(arr)

    for i in permu:
        if i == sorted(i):
            return i


    