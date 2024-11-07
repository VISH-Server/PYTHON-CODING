def generate_lucky_numbers(n):
    series = list(range(1, n + 1))
    step = 2
    while len(series) >= step:
        del_index = step - 1
        series = [series[i] for i in range(len(series)) if (i + 1) % step != 0]
        step += 1

    return series

user_input = int(input("Enter the value of n: "))
result_series = generate_lucky_numbers(user_input)

print(f"Lucky Numbers up to {user_input}: {result_series}")
