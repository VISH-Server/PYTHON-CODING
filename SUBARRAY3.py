def print_subarrays_with_distinct_elements(arr):
    n = len(arr)
    result = []

    for i in range(n):
        visited = set()
        current_subarray = []

        for j in range(i, n):
            if arr[j] not in visited:
                visited.add(arr[j])
                current_subarray.append(arr[j])
            else:
                break

        if len(current_subarray) == len(visited):
            result.append(current_subarray)

    print("The largest subarrays with all distinct elements are:")
    for subarray in result:
        print("{", end=" ")
        for element in subarray:
            print(element, end=" ")
        print("}")

# Example usage
input_array = [5, 2, 3, 5, 4, 3]
print_subarrays_with_distinct_elements(input_array)
