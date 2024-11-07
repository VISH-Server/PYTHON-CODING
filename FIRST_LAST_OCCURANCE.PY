def find_first_last_occurrence(arr, key):
    def binary_search_left(arr, key):
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == key:
                result = mid
                right = mid - 1
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return result

    def binary_search_right(arr, key):
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == key:
                result = mid
                left = mid + 1
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return result

    left_occurrence = binary_search_left(arr, key)
    right_occurrence = binary_search_right(arr, key)

    if left_occurrence != -1:
        return [left_occurrence, right_occurrence]
    else:
        return [-1, -1]


arr = [1, 2, 3, 3, 3, 4, 4, 5]
key1 = 3
key2 = 5
key3 = 6
print(find_first_last_occurrence(arr, key1))  
print(find_first_last_occurrence(arr, key2))  
print(find_first_last_occurrence(arr, key3))  
