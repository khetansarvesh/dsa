"""
Recursive Merge Sort Implementation

This implementation includes:
1. merge: Imported from 2_pointers module (merges two separate sorted vectors)
2. merge_within: Merges sorted portions within a single vector
3. merge_sort: Recursively sorts the array using merge sort
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / '2_pointers'))
from merge_sorted_arrays import merge


def merge_within(v, int_1, int_mid, int_r):
    """
    Merge two sorted portions within a single vector
    
    v: the vector containing both sorted portions
    int_1: start index of first portion
    int_mid: end index of first portion (mid point)
    int_r: end index of second portion
    """
    # Create temporary vectors for the two halves
    temp_vector_1 = []
    for i in range(int_1, int_mid + 1):
        temp_vector_1.append(v[i])
    
    temp_vector_2 = []
    for i in range(int_mid + 1, int_r + 1):
        temp_vector_2.append(v[i])
    
    # Merge the two temporary vectors
    v_merged_within = merge(temp_vector_1, temp_vector_2)
    
    # Copy merged elements back to original vector
    for i in range(len(v_merged_within)):
        v[int_1 + i] = v_merged_within[i]


def merge_sort(v, int_l, int_r):
    """
    Recursively sort array using merge sort
    
    v: array to sort
    int_l: left index
    int_r: right index
    """
    # Base case
    if int_l >= int_r:
        return
    
    # Find middle point
    int_m = (int_l + int_r) // 2
    
    # Recursively sort first half
    merge_sort(v, int_l, int_m)
    
    # Recursively sort second half
    merge_sort(v, int_m + 1, int_r)
    
    # Merge the two sorted halves
    merge_within(v, int_l, int_m, int_r)