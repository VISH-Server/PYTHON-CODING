def lcs(A, B, str1, str2):
    dp = [[0] * (B + 1) for _ in range(A + 1)]
    
    for i in range(1, A + 1):
        for j in range(1, B + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[A][B]

str1_1 = "ABCDGH"
str2_1 = "AEDFHR"
A1 = len(str1_1)
B1 = len(str2_1)
print(lcs(A1, B1, str1_1, str2_1))  

str1_2 = "ABC"
str2_2 = "AC"
A2 = len(str1_2)
B2 = len(str2_2)
print(lcs(A2, B2, str1_2, str2_2))  

str1_2 = "ABC"
str2_2 = "ACB"
A2 = len(str1_2)
B2 = len(str2_2)
print(lcs(A2, B2, str1_2, str2_2))
