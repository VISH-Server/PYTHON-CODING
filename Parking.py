def find_row_with_max_ones(R, C, elements):
    matrix = []
    for i in range(R):
        row = elements[i * C:(i + 1) * C]
        matrix.append(row)
    
    max_ones = -1
    row_index = -1
    for i in range(R):
        count_ones = sum(matrix[i])
        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i + 1  
    return row_index

# Example usage:
R = 3
C = 3
elements = [0, 1, 0, 1, 1, 0, 1, 1, 1]
print(find_row_with_max_ones(R, C, elements))  

R = 4
C = 3
elements = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]
print(find_row_with_max_ones(R, C, elements))  

R = 4
C = 3
elements = [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1]
print(find_row_with_max_ones(R, C, elements))  

R = 4
C = 3
elements = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1]
print(find_row_with_max_ones(R, C, elements))  