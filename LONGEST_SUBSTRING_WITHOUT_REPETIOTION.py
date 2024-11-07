def longest_unique_substring(s):
    l, r, n, ans = 0, 0, len(s), -1
    st = ""
    char_count = {}
    
    while r < n:
        if s[r] in char_count and char_count[s[r]] >= 1:
            char_count[s[l]] -= 1
            l += 1
        
        char_count[s[r]] = char_count.get(s[r], 0) + 1
        
        if ans < r - l + 1:
            ans = r - l + 1
            st = s[l:r+1]
        
        r += 1
    
    return ans, st

if __name__ == "__main__":
    s = input()
    length, substring = longest_unique_substring(s)
    print(f"{length}({substring})")
