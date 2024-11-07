def find_smallest_element_greater_than_key(arr, key):
    left, right = 0, len(arr) - 1
    result = float('inf')  

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > key:
            result = min(result, arr[mid])
            right = mid - 1
        else:
            left = mid + 1

    if result == float('inf'):
        return key 
    else:
        return result

arr1 = [1, 2, 3, 3, 4, 4, 8, 10]
key1 = 4
key2 = 5
key3 = -5
print(find_smallest_element_greater_than_key(arr1, key1))  
print(find_smallest_element_greater_than_key(arr1, key2))  
print(find_smallest_element_greater_than_key(arr1, key3))  
