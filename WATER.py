def maxArea(height):
    n = len(height)
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            h = min(height[i], height[j]) 
            width = j - i
            area = h * width
            
            max_area = max(max_area, area)
    
    return max_area
height1 = [1,8,6,2,5,4,8,3,6]
print(maxArea(height1)) 

height2 = [1,1]
print(maxArea(height2)) 

height3 = [1,2,4,3,5,7,9,8,1]
print(maxArea(height3
              ))