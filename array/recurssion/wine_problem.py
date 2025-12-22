def wine_problem(price, l, r, yr):
    # Base case: only one wine left
    if l == r:
        return yr * price[l]
    
    # Recursion: Choose max of selling left wine or right wine
    return max(
        yr * price[l] + wine_problem(price, l + 1, r, yr + 1),  # Sell left wine
        yr * price[r] + wine_problem(price, l, r - 1, yr + 1)   # Sell right wine
    )