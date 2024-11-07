def decode_string(encoded_str):
    stack = []
    current_num = 0
    current_str = ""

    for char in encoded_str:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_num, current_str))
            current_num = 0
            current_str = ""
        elif char == ']':
            count, prev_str = stack.pop()
            current_str = prev_str + current_str * count
        else:
            current_str += char

    return current_str

encoded_str = input("Enter the encoded string: ")

decoded_str = decode_string(encoded_str)

print("Decoded string:", decoded_str)
