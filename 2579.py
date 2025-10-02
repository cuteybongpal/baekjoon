a = int(input())
stairs = []
for i in range(a):
    stairs.append(int(input()))
dp = [0] * a
dp[0] = stairs[0]
if a > 1:
    dp[1] = dp[0] + stairs[1]
if a > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
#시발시발시발시발시발시발시발시발십라빗방벌;ㅣㅏㅁㅇㄴㄹ';ㄷ
for i in range(3, a):
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]
    
print(dp)
print(dp[-1])