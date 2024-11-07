def count_permutations(arr, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
        for num in arr:
            if i >= num:
                dp[i] += dp[i - num]

    return dp[target]

arr = [1, 2, 3, 4]
target = 3
output = count_permutations(arr, target)
print(output)

arr = [1, 3, 5]
target = 5
output = count_permutations(arr, target)
print(output)

arr = [1, 2, 3, 4, 5]
target = 5
output = count_permutations(arr, target)
print(output)