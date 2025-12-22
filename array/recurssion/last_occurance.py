"""
Find the last occurrence of an element in an array using recursion

v : array
last_occurance_of : element to find
r : right pointer index (starts from end of array)
"""

def last_occurance(v, last_occurance_of, r):
    # Base case: reached before the start of array
    if r == -1:
        print("Not present")
        return -1
    
    # If current element matches, return the index
    if v[r] == last_occurance_of:
        return r
    
    # Recursively check previous elements
    return last_occurance(v, last_occurance_of, r - 1)