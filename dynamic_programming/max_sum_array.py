# Given an array of integers, find the subset of non-adjacent elements with the maximum sum. 
# Calculate the sum of that subset. It is possible that the maximum sum is 0, the case when all elements are negative.

def maxSubsetSum(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    if n == 1:
        return max(0, arr[0])

    max_sum_with_curr = max(0, arr[0])
    max_sum_without_curr = 0
    
    for i in range(1, n):
        new_max_sum_with_curr = max(max_sum_without_curr + arr[i], max_sum_with_curr)
        max_sum_without_curr = max(max_sum_with_curr, max_sum_without_curr)
        
        max_sum_with_curr = new_max_sum_with_curr
    return max(max_sum_with_curr, max_sum_without_curr)

test_arr = [-2, 1, 3, -4, 5]

print(maxSubsetSum(test_arr))