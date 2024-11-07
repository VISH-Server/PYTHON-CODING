def is_symmetrical(input_str):
    length = len(input_str)
    if length % 2 == 0:
        return input_str[:length // 2] == input_str[length // 2:]
    else:
        return input_str[:length // 2] == input_str[length // 2 + 1:][::-1]

def is_palindrome(input_str):
    return input_str == input_str[::-1]


input_str = "khokho"

if is_symmetrical(input_str):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if is_palindrome(input_str):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")


input_str = "aaaaa"

if is_symmetrical(input_str):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if is_palindrome(input_str):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")
