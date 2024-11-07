def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]

    return -1  

# Example usage:
arr = [2, 4, 5, 1, 2, 3]
result = find_equilibrium_index(arr)

if result != -1:
    print(f"Equilibrium index is: {result}")
else:
    print("No equilibrium index found.")
