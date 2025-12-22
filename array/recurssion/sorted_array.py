def sorted_or_not(v, r):
    if r == 0:
        return True
    
    if sorted_or_not(v, r - 1) and v[r] > v[r - 1]:
        return True
    
    return False