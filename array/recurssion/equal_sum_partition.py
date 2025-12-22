import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from subset_sum import subset_sum


def equal_sum_partition(arr):

    # Calculate total sum
    total_sum = sum(arr)
    
    # If total sum is odd, equal partition is impossible
    if total_sum % 2 != 0:
        return False
    
    # If total sum is even, check if subset with sum = total_sum/2 exists
    target_sum = total_sum // 2
    
    return subset_sum(arr, target_sum, len(arr) - 1)