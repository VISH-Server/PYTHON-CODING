def find_largest_subarray(arr):
    n = len(arr)
    max_length = 0
    start_index = 0

    for i in range(n):
        current_start = i
        current_set = set()
        current_length = 0

        for j in range(i, n):
            if arr[j] in current_set:
                break
            current_set.add(arr[j])
            current_length += 1

            if current_length > max_length:
                max_length = current_length
                start_index = current_start

    return arr[start_index:start_index + max_length]

def main():
    input_array = [1, 2, 3, 4, 5, 1, 2, 3]
    result = find_largest_subarray(input_array)

    print(f"The largest subarray is: {result}")

if __name__ == "__main__":
    main()
