def max_possible_score(N, A):
    # Initialize the dp array with negative infinity
    dp = [float('-inf')] * N
    dp[0] = 0  # Starting point, no score yet
    
    # Iterate through each position i in the array
    for i in range(N):
        # For each position i, try to jump to all positions j such that i < j <= i + A[i]
        for j in range(i + 1, min(i + A[i] + 1, N)):
            # Update dp[j] with the maximum score possible by jumping from i to j
            dp[j] = max(dp[j], dp[i] + A[i] * A[j])
    
    # The result is the maximum score to reach the last index
    return dp[N - 1]

# Example usage:
import sys
input = sys.stdin.read
data = input().split()

# Extracting the input
N = int(data[0])
A = list(map(int, data[1:]))

# Call the function and print the result
print(max_possible_score(N, A))
