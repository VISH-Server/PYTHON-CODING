def longest_substring(s):
    if not s:
        return 0, ""

    char_index = {}  
    start = 0  
    max_l = 0 
    max_ss = ""
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end
        current_l = end - start + 1

        if current_l > max_l:
            max_l = current_l
            max_ss = s[start:end+1]

    return max_l, max_ss
input_string = "characteristics"
length, substring = longest_substring(input_string)
print("Length of the longest substring:", length)
print("Longest substring:", substring)
