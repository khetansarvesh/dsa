def coinmax(a, l, r):

    # Base case: only 2 coins left
    if (r - l) == 1:
        return max(a[l], a[r])
    
    # Recursive case:
    return max(
        a[l] + min(coinmax(a, l + 2, r), coinmax(a, l + 1, r - 1)),
        a[r] + min(coinmax(a, l + 1, r - 1), coinmax(a, l, r - 2))
    )