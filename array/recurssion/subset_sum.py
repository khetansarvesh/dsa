"""
Check if there exists a subset with the given sum

arr: array of integers
target_sum: target sum to achieve
r: current index (starts from last element)

Returns: True if subset exists, False otherwise
"""

def subset_sum(arr, target_sum, r):

    # Base case 1: If target sum is 0, we found a valid subset
    if target_sum == 0:
        return True
    
    # Base case 2: If no elements left and sum is not 0
    if r == -1:
        return False
    
    # 2 branch condition: If current element is less than or equal to target
    if arr[r] <= target_sum:
        # Include current element OR exclude current element
        return (
            subset_sum(arr, target_sum - arr[r], r - 1) or
            subset_sum(arr, target_sum, r - 1)
        )
    
    # 1 branch condition: If current element is greater than target, skip it
    if arr[r] > target_sum:
        return subset_sum(arr, target_sum, r - 1)