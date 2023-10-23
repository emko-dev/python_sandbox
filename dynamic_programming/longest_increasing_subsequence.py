# Given an integer array nums, return the length of the longest strictly increasing subsequence
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
from utils.utils import measure_execution_time

# O(n^2)
# Outer loop runs for each element in the nums array, so it has a time complexity of O(n).
# Inner loop that iterates through all elements before the current element (from index 0 to i - 1).
# In the worst case, this inner loop will run up to i times for each element in the outer loop.
@measure_execution_time
def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    current_lis = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                current_lis[i] = max(current_lis[i], current_lis[j] + 1)

    return max(current_lis)


# O(n log(n))
# Maintain an array (tail) to store the smallest and largest elements of a potential strictly increasing subsequence.
# For each element, use binary search to find the correct position for the element within the tail array.
# If the current element is smaller than the smallest element in the tail, update the smallest element.
# If the current element is larger than the largest element in the tail, append it to the tail.
@measure_execution_time
def binary_search_length_of_list(nums):
    if not nums:
        return 0

    n = len(nums)
    tail = [0] * n
    length = 1
    tail[0] = nums[0]

    for i in range(1, n):
        if nums[i] < tail[0]:
            tail[0] = nums[i]
        elif nums[i] > tail[length - 1]:
            tail[length] = nums[i]
            length += 1
        else:
            index = binary_search(tail, 0, length - 1, nums[i])
            tail[index] = nums[i]

    return length

def binary_search(arr, left, right, x):
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


input_list = [10,9,2,5,3,7,101,18]
list500 = [i for i in range(1, 501)]
print(length_of_lis(list500))
print(binary_search_length_of_list(list500))