"""
Recursive Insertion Sort Implementation

This implementation uses two recursive functions:
1. insert_at_right_position: Inserts an element at the correct position in a sorted array
2. sort_array: Recursively sorts the array using insertion sort
"""

def insert_at_right_position(v, r, ele_to_insert):
    """
    Insert an element at the right position in a sorted array
    
    v: array (sorted up to index r)
    r: current index to check
    ele_to_insert: element to insert
    """
    # Finding the right index to place the element
    i = 0
    while v[i] < ele_to_insert:
        i += 1
    
    pos_to_insert_at = i
    
    # Inserting at that index
    if pos_to_insert_at == r:
        v[pos_to_insert_at] = ele_to_insert
        return
    else:
        # Shift elements to the right
        for j in range(r, pos_to_insert_at, -1):
            v[j] = v[j - 1]
        v[pos_to_insert_at] = ele_to_insert
        return


def sort_array(v, r):
    """
    Recursively sort array using insertion sort
    
    v: array to sort
    r: right index (current position)
    """
    # Base case
    if r == -1:
        return
    
    # Store the last element
    ele = v[r]
    
    # Recursive call to sort array up to r-1
    sort_array(v, r - 1)
    
    # Inserting the element at right position
    insert_at_right_position(v, r, ele)
    return