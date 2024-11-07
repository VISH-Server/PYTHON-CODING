def min_subarray_length(nums, target):
    if not nums:
        return 0

    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1

    return min_length if min_length != float('inf') else 0

# Example usage:

array1 = [3, 1, 7, 1, 2]
target1 = 11
output1 = min_subarray_length(array1, target1)
print(output1)  


array2 = [2, 3, 5, 4, 1]
target2 = 10
output2 = min_subarray_length(array2, target2)
print(output2) 

array1 = [7, 4, 1, 5, 2]
target1 = 16
output1 = min_subarray_length(array1, target1)
print(output1)  

array2 = [9, 8, 6, 1, 2]
target2 = 24
output2 = min_subarray_length(array2, target2)
print(output2) 

