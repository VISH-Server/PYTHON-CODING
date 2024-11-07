def count_repeated_words(input_string):
    w = input_string.split()
    w_count = {}
    non_repeated_words = []
    for wd in w:
        c_word = wd.strip(".?!//;").lower()
        if c_word in w_count:
            w_count[c_word] += 1
        else:
            w_count[c_word] = 1
            non_repeated_words.append(wd)
    print("Count of repeated words:")
    for wd, count in w_count.items():
        if count > 1:
            print(f"{wd}: {count}")
    print("\nString without repeated words:")
    print(" ".join(non_repeated_words))
count_repeated_words("HE IS A GOOD BOY .HE GOES TO SCHOOL EVERY DAY")
