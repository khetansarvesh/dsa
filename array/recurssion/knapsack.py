def knapsack(weight, value, knapsack_weight, r):

    # Base case 1: If knapsack capacity is 0
    if knapsack_weight == 0:
        return 0
    
    # Base case 2: If no items left to consider
    if r == -1:
        return 0
    
    # 2 branch condition
    if weight[r] <= knapsack_weight:
        return max(
            value[r] + knapsack(weight, value, knapsack_weight - weight[r], r - 1),
            knapsack(weight, value, knapsack_weight, r - 1)
        )
    
    # 1 branch condition
    if weight[r] > knapsack_weight:
        return knapsack(weight, value, knapsack_weight, r - 1)