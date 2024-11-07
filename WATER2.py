def trappingWater(arr, n):
    l_max = [0] * n 
    r_max = [0] * n 
    l_max[0] = arr[0]
    for i in range(1, n):
        l_max[i] = max(l_max[i - 1], arr[i])
    
    r_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        r_max[i] = max(r_max[i + 1], arr[i])
    
    water_trapped = 0
    for i in range(n):
        water_trapped += min(l_max[i], r_max[i]) - arr[i]
    
    return water_trapped


arr1 = [3, 0, 0, 2, 0, 4]
n1 = len(arr1)
print(trappingWater(arr1, n1)) 

arr2 = [7, 4, 0, 9]
n2 = len(arr2)
print(trappingWater(arr2, n2))  

arr3 = [6, 9, 9]
n3 = len(arr3)
print(trappingWater(arr3, n3))  
