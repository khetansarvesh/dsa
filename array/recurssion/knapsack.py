def knapsack(weight, value, knapsack_weight, r):

    # Base case 1: If knapsack capacity is 0
    if knapsack_weight == 0:
        return 0
    
    # Base case 2: If no items left to consider
    if r == -1:
        return 0
    
    # Recursion: If current item's weight fits in knapsack
    if weight[r] <= knapsack_weight:
        # Take maximum of:
        # 1. Include current item: value[r] + knapsack with reduced weight
        # 2. Exclude current item: knapsack without this item
        return max(
            value[r] + knapsack(weight, value, knapsack_weight - weight[r], r - 1),
            knapsack(weight, value, knapsack_weight, r - 1)
        )
    
    # Recursion: If current item is too heavy, skip it
    if weight[r] > knapsack_weight:
        return knapsack(weight, value, knapsack_weight, r - 1)