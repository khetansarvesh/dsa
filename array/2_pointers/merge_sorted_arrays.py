"""
Two Pointers: Merge Two Sorted Arrays

Classic two-pointer algorithm to merge two sorted arrays into one sorted array.
"""

def merge(v1, v2):
    """
    Merge two sorted vectors into one sorted vector
    
    v1: first sorted vector
    v2: second sorted vector
    Returns: merged sorted vector
    """
    v_merged = []
    i = 0
    j = 0
    
    # Merge elements from both vectors while both have elements
    while i < len(v1) and j < len(v2):
        if v1[i] <= v2[j]:
            v_merged.append(v1[i])
            i += 1
        
        if v2[j] <= v1[j]:
            v_merged.append(v2[j])
            j += 1
    
    # Add remaining elements from v1
    while i < len(v1):
        v_merged.append(v1[i])
        i += 1
    
    # Add remaining elements from v2
    while j < len(v2):
        v_merged.append(v2[j])
        j += 1
    
    return v_merged
