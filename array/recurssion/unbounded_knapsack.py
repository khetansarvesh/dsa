# Unbounded Knapsack - items can be used multiple times
def unbounded_knapsack(weight, value, knapsack_weight, r):

    # Base case 1: If knapsack capacity is 0
    if knapsack_weight == 0:
        return 0
    
    # Base case 2: If no items left to consider
    if r == -1:
        return 0
    
    # 2 branch condition: If current item fits
    if weight[r] <= knapsack_weight:
        return max(
            # *** KEY DIFFERENCE: After taking item, we stay at index r (not r-1) ***
            # This allows us to take the same item again
            value[r] + unbounded_knapsack(weight, value, knapsack_weight - weight[r], r),
            
            # Exclude current item and move to next
            unbounded_knapsack(weight, value, knapsack_weight, r - 1)
        )
    
    # 1 branch condition: If current item is too heavy, skip it
    if weight[r] > knapsack_weight:
        return unbounded_knapsack(weight, value, knapsack_weight, r - 1)