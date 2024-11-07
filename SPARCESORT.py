def sparse_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == "":
            l_search, r_search = mid - 1, mid + 1
            while True:
                if l_search < l and r_search > r:
                    return -1  
                elif r_search <= r and arr[r_search] != "":
                    mid = r_search
                    break
                elif l_search >= l and arr[l_search] != "":
                    mid = l_search
                    break
                l_search -= 1
                r_search += 1

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1 


arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
target = "ball"
result = sparse_search(arr, target)
print("Output:", result)


arr = ["my ", "", "name", "", "is", "", "", "bhoba", "roy", "", "rudra", "", ""]
target = "bhoba"
result = sparse_search(arr, target)
print("Output:", result)


arr = ["", "", "", "", "", "", "", "", "", "", "q", "", ""]
target = "a"
result = sparse_search(arr, target)
print("Output:", result)


arr = ["Hlo", "", "how", "r", "", "", "u","", "", "", "", "", ""]
target = "u"
result = sparse_search(arr, target)
print("Output:", result)
