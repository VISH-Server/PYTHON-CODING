class Solution:
    def rearrange(nums):
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0


# Example usage:

arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
Solution.rearrange(arr)
print(arr)

arr = [0, 7, 6, 8, 2, 3, 1, 0, 1]
Solution.rearrange(arr)
print(arr)

arr = [0, 0, 0, 2, 3, 0, 4, 0, 1]
Solution.rearrange(arr)
print(arr)

arr = [6, 5, 8, 2, 3, 7, 4, 2, 1]
Solution.rearrange(arr)
print(arr)
