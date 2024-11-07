def TWO_UNIQUE_NO(arr):
    ncount = {}    
    for num in arr:
        if num in ncount:
            ncount[num] += 1
        else:
            ncount[num] = 1

    a = None
    b = None

    for num in arr:
        if ncount[num] == 1:
            a = num
            break

    if a is not None:
        for num in arr:
            if num != a and ncount[num] == 1:
                b = num
                break

    return (a, b)

user_input = input("Enter numbers ")
user_input = user_input.split()
user_input = [int(num) for num in user_input]

a, b = TWO_UNIQUE_NO(user_input)

if a is None:
    print("No unique numbers found in the array.")
elif b is None:
    print(f"The second unique number is not available. The first unique number is: {a}")
else:
    print(f"The first unique number is: {a}")
    print(f"The second unique number is: {b}")
