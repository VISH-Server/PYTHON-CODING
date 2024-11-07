def are_eq(x, y):
    return not (x ^ y)

# Example usage 1:
num1 = 5
num2 = 5

if are_eq(num1, num2):
    print("Equal.")
else:
    print("Not equal.")


# Example usage 2:
num1 = 9
num2 = 5

if are_eq(num1, num2):
    print("Equal.")
else:
    print("Not equal.")

# Example usage 3:
num1 = 5
num2 = 3

if are_eq(num1, num2):
    print("Equal.")
else:
    print("Not equal.")

