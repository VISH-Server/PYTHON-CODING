def find_largest_subarray_with_equal_zeros_ones(arr):
    # Create a dictionary to store the running sum along with its corresponding index
    sum_dict = {0: -1}
    max_len = 0
    end_index = -1
    running_sum = 0

    for i in range(len(arr)):
        running_sum += 1 if arr[i] == 1 else -1

        if running_sum in sum_dict:
            current_len = i - sum_dict[running_sum]
            if current_len > max_len:
                max_len = current_len
                end_index = i

        else:
            sum_dict[running_sum] = i

    start_index = end_index - max_len + 1
    largest_subarray = arr[start_index:end_index + 1]

    return largest_subarray

# Example usage
input_array = [0, 0, 1, 0, 1, 0, 0]
output_array = find_largest_subarray_with_equal_zeros_ones(input_array)
print("The largest subarray is:", output_array)
