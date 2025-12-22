''' Method 1

v : array
r : right pointer index
'''
def sorted_or_not(v, r):
    if r == 0:
        return True
    
    if sorted_or_not(v, r - 1) and v[r] > v[r - 1]:
        return True
    
    return False


''' Method 2

v : array
l : left pointer index
'''
def sorted_or_not_v2(v, l):
    if l == len(v) - 1:
        return True
    
    if sorted_or_not_v2(v, l + 1) and v[l] < v[l + 1]:
        return True
    
    return False