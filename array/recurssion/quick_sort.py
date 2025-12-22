"""
Recursive Quick Sort Implementation

This implementation uses the partitioning algorithm:
1. partition: Partitions array around a pivot element
2. quick_sort: Recursively sorts using divide-and-conquer
"""

def partition(arr, l, h):
    """
    Partition the array around a pivot element
    
    arr: array to partition
    l: left index (start)
    h: right index (end)
    Returns: partition index
    """
    # Choose the last element as pivot
    pivot = arr[h]
    i = l
    j = h
    
    while True:
        # Find element from left that is greater than pivot
        while arr[i] <= pivot:
            i += 1
        
        # Find element from right that is smaller than pivot
        j -= 1
        while arr[j] > pivot:
            if i < j:
                # Swap elements
                arr[i], arr[j] = arr[j], arr[i]
        
        # When pointers cross, break
        if i >= j:
            break
    
    # Swap pivot with element at i
    arr[i], arr[h] = arr[h], arr[i]
    
    return i


def quick_sort(arr, l, h):
    """
    Recursively sort array using quicksort
    
    arr: array to sort
    l: left index
    h: right index
    """
    if l < h:
        # Partition the array and get partition index
        j = partition(arr, l, h)
        
        # Recursively sort left side
        quick_sort(arr, l, j - 1)
        
        # Recursively sort right side
        quick_sort(arr, j + 1, h)