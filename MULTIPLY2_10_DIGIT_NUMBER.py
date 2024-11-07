def multiply_strings(num1: str, num2: str) -> str:
    num1_int = int(num1)
    num2_int = int(num2)

    result_int = num1_int * num2_int

    result_str = str(result_int)

    return result_str

# Test the function
num1 = "1234567890"
num2 = "9876543210"
result = multiply_strings(num1, num2)
print("Result:", result)
