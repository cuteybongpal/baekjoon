word1 = input()
word2 = input()
dp = []
if len(word1) > len(word2):
    for i in range(len(word1)+1):
        dp.append([0] * (len(word1) + 1))
else:
    for i in range(len(word2)+1):
        dp.append([0] * (len(word2) + 1))

for i in range(1, len(dp)):
    for j in range(1, len(dp)):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if i > len(word1) or j > len(word2):
            continue
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[-1][-1])