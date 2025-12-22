def count_subset_sum(arr, target_sum, r):

    # Base case 1: If target sum is 0, we found one valid subset (empty subset)
    if target_sum == 0:
        return 1
    
    # Base case 2: If no elements left and sum is not 0
    if r == -1:
        return 0
    
    # 2 branch condition: If current element is less than or equal to target
    if arr[r] <= target_sum:
        # Count subsets that include current element + subsets that exclude it
        return (
            count_subset_sum(arr, target_sum - arr[r], r - 1) +
            count_subset_sum(arr, target_sum, r - 1)
        )
    
    # 1 branch condition: If current element is greater than target, skip it
    if arr[r] > target_sum:
        return count_subset_sum(arr, target_sum, r - 1)