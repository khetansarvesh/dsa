# Coin Change Problem - Count number of ways to make change
def coin_change(coins, amount, r):
    """
    Count number of ways to make change for given amount using given coins
    Each coin can be used UNLIMITED times (unbounded)
    
    coins: list of coin denominations
    amount: target amount
    r: current coin index
    
    Returns: number of ways to make change
    """
    # Base case 1: If amount is 0, we found one way
    if amount == 0:
        return 1
    
    # Base case 2: If no coins left
    if r == -1:
        return 0
    
    # 2 branch condition: If current coin fits
    if coins[r] <= amount:
        return (
            # *** KEY DIFFERENCE FROM SUBSET SUM: After using coin, stay at r (not r-1) ***
            # This allows us to use the same coin again (unbounded)
            coin_change(coins, amount - coins[r], r) +
            
            # Skip current coin and move to next
            coin_change(coins, amount, r - 1)
        )
    
    # 1 branch condition: If current coin is too large, skip it
    if coins[r] > amount:
        return coin_change(coins, amount, r - 1)